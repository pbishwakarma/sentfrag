from datetime import datetime
from enum import Enum

class Document(object):

    def __init__(self):
        self.__init__(None, None)

    def __init__(self, filepath, author):
        self.filepath = filepath
        self.author = author
        self.created = datetime.now()
        self._score = 0

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, score):
        self._score = score


class Sentence(object):

    def __init__(self, sentence):
        if type(sentence) != str or len(sentence) == 0:
            raise ValueError("Sentence must be a non-empty string")

        self._raw = sentence
        self._tokenized = None
        self._pos = None
        self._chunks = None

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