class TXTReader():

    def __init__(self, filepath):
        self._filepath = filepath

    def read(self):
        with open(self._filepath) as f:
            text = f.read()

        return text

SUPPORTED_READERS = {
    "txt": TXTReader
}