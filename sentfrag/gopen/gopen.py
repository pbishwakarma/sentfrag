from sentfrag.gopen.nlp import tokenize, tag, chunk
from sentfrag.infra.document import Sentence

class Gopen(object):

    def __init__(self):
        pass
        
    def label(self, sentence: Sentence):
        if not isinstance(sentence, Sentence):
            raise ValueError("Input must be of type Sentence")

        raw = sentence.get_raw()
        print(raw)
        words = tokenize(raw)
        print(words)
        print(type(words))
        tagged = tag(words)
        print(tagged)
        chunked = chunk(tagged)

        sentence.set_tokenized(words)
        sentence.set_pos(tagged)
        sentence.set_chunks(chunked)

        return chunked

if __name__ == "__main__":
    sent = "The boy plays right wing on his soccer team"
    gopen = Gopen()
    sentence = Sentence(sent)
    chunked = gopen.label(sentence)
    print(chunked)



