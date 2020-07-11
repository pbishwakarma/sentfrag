from sentfrag.gopen.nlp import tokenize, tag, chunk
from sentfrag.infra.document import Sentence
from sentfrag.infra.constants import BACKWARDS_LINK, STRESS_POSITION, SUBJECT, VERB, LABELS
from sentfrag.gopen.tagset import PENN_BANK


class Gopen(object):

    def __init__(self, tagset=PENN_BANK):        
        self._tagset = tagset
        
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

    
    def label(self, sentence: Sentence, get_back_link: bool):
        chunked = sentence.get_chunks()
        if not chunked:
            self._label(sentence, get_back_link)
        
        sentence.set_label(SUBJECT, self.get_subject(sentence))
        sentence.set_label(VERB, self.get_verb(sentence))
        sentence.set_label(STRESS_POSITION, self.get_stress_position(sentence))
        
        if get_back_link:
            sentence.set_label(BACKWARDS_LINK, self.get_backward_link(sentence))

        return sentence

    def get_backward_link(self, sentence: Sentence):
        pass

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


if __name__ == "__main__":
    sentence = Sentence("The boy that plays uncharted shoots the gun at the enemy")
    g = Gopen()
    labeled = g.label(sentence, False)
    print(labeled)



