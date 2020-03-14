from nltk.tokenize import sent_tokenize

class Reader(object):

    def __init__(self, filepath, out_dir):
        self.filepath = filepath
        self.out_dir = out_dir
        
    def read(self, text):
        """
        Reads the provided text and returns a generator of strings. Each entry
        contains a sentence.

        Args:
            text (str): The text from the infile.

        Returns:
            list: generator of sentences split by punctuation marks.
        """
        for sentence in sent_tokenize(text):
            yield sentence.strip()

class PDFReader(Reader):

    def __init__(self, file, out_dir):
        super().__init__(file, out_dir)

    def read(self):
        text = "foo bar."
        return super().read(text)

class TXTReader(Reader):

    def __init__(self, file, out_dir):
        super().__init__(file, out_dir)

    def read(self):
        with open(self.filepath) as f:
            text = f.read()

        return super().read(text)

