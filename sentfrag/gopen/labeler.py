import logging
from typing import Optional

from sentfrag.gopen.nlp import tokenize, tag, chunk, embed
from sentfrag.infra.document import Document, Sentence
from sentfrag.infra.constants import BACKWARDS_LINK, STRESS_POSITION, SUBJECT, VERB, LABELS
from sentfrag.gopen.tagset import PENN_BANK

from scipy import spatial

class Labeler(object):

    def __init__(self, model, tagset=PENN_BANK):        
        self._tagset = tagset
        self.logger = logging.getLogger(self.__class__.__name__)
        self.model = model
        
    def _label(self, sentence: Sentence, get_back_link: bool):
        if not isinstance(sentence, Sentence):
            raise ValueError("Input must be of type Sentence")

        raw = sentence.get_raw()
        words = tokenize(raw)
        tagged = tag(words)
        chunked = chunk(tagged)

        sentence.set_tokenized(words)
        sentence.set_pos(tagged)
        sentence.set_chunks(chunked)

    def label(self, sentence: Sentence, prev_sentence: Optional[Sentence], get_back_link: bool):
        chunked = sentence.get_chunks()
        if not chunked:
            self._label(sentence, get_back_link)
        
        sentence.set_label(SUBJECT, self.get_subject(sentence))
        sentence.set_label(VERB, self.get_verb(sentence))
        sentence.set_label(STRESS_POSITION, self.get_stress_position(sentence))
        
        if get_back_link and prev_sentence:
            sentence.set_label(BACKWARDS_LINK, self.get_backward_link(sentence, prev_sentence))

        return sentence

    def get_backward_link(self, sentence: Sentence, prev: Sentence):
        parts = sentence.get_chunks()
        prev_embedding = embed(self.model, [prev.get_raw()])
        score = 0
        back_link = None
        try:
            for part in parts:
                if isinstance(part, tuple):
                    phrase = part[0]
                else:
                    phrase = " ".join(word[0] for word in part.leaves())
                
                phrase_embedding = embed(self.model, [phrase])
                phrase_score = 1 - spatial.distance.cosine(prev_embedding, phrase_embedding)
                if phrase_score > score:
                    score = phrase_score
                    back_link = phrase
        except Exception as e:
            self.logger.warn("Error encountered while calculating backwards link")

        return back_link


    def get_subject(self, sentence: Sentence):
        chunks = sentence.get_chunks()
        nounphrases = chunks.subtrees(filter = lambda x : x.label() == "NP")
        subject_node = next(nounphrases, None)
        subject = " ".join(word[0] for word in subject_node.leaves())
        
        return subject

    def get_verb(self, sentence: Sentence):
        chunks = sentence.get_chunks()
        leaves = chunks.leaves()
        for i in range(len(leaves)):
            if str(leaves[i][1]) in self._tagset.get(VERB):
                return leaves[i][0]
        
        return None

    def get_stress_position(self, sentence: Sentence):
        chunks = sentence.get_chunks()
        nounphrases = chunks.subtrees(filter = lambda x: x.label() == "NP")
        *_, last_node =  nounphrases
        sp = " ".join(word[0] for word in last_node.leaves())
        return sp


