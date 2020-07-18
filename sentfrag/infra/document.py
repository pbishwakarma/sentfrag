from datetime import datetime
from enum import Enum
from sentfrag.infra.constants import VERB, STRESS_POSITION, BACKWARDS_LINK, SUBJECT, LABEL_VALUE, LABEL_INDEX, LABEL_LEN, LABELS

class Document(object):

    def __init__(self):
        self.__init__(None, None)

    def __init__(self, filepath, author=None):
        self.filepath = filepath
        self.author = author
        self.created = datetime.now()
        self._score = 0
        self._sentences = []

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, score):
        self._score = score

    def set_sentences(self, sentences: list):
        self._sentences = sentences

    def get_sentences(self):
        return self._sentences
        
    def set_author(self, author):
        self.author = author

    def get_author(self):
        return self.author

class Sentence(object):

    def __init__(self, sentence):
        if type(sentence) != str or len(sentence) == 0:
            raise ValueError("Sentence must be a non-empty string")

        self._raw = sentence
        self._words = sentence.split()
        self._tokenized = None
        self._pos = None
        self._chunks = None

        # Indices of sentence componenets
        self._labels = {
            STRESS_POSITION: {},
            VERB: {},
            SUBJECT: {},
            BACKWARDS_LINK: {}
        }

    def set_label(self, label, value):
        if label in LABELS and value:
            label_len = len(value)
            label_index = self._raw.find(value)
            self._labels[label] = {
                LABEL_INDEX: label_index,
                LABEL_VALUE: value,
                LABEL_LEN: label_len
            }
    
    def get_labels(self):
        return self._labels

    def get_label(self, label):
        return self._labels.get(label, None)

    def get_raw(self):
        return self._raw

    def set_tokenized(self, tokenized):
        self._tokenized = tokenized

    def get_tokenized(self):
        return self._tokenized

    def set_chunks(self, chunks):
        self._chunks = chunks

    def get_chunks(self):
        return self._chunks

    def set_pos(self, pos):
        self._pos = pos
        
    def get_pos(self):
        return self._pos

    def __str__(self):
        return f"""
        Raw: {self._raw}
        
        Subject: {self._labels.get(SUBJECT)}
        Verb: {self._labels.get(VERB)}
        Stress Position: {self._labels.get(STRESS_POSITION)}
        Backwards Link: {self._labels.get(BACKWARDS_LINK)}
        """
            