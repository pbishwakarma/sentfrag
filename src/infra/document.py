from datetime import datetime

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
