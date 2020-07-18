from string import punctuation
from typing import Optional

from sentfrag.infra.document import Document, Sentence
from sentfrag.gopen.labeler import Labeler
from sentfrag.preprocessors.readers import PDFReader, TXTReader, SUPPORTED_READERS


class DocumentBuilder(object):

    def __init__(self):
        pass

    
    def _label_sentence(self, prev_sent: Optional[Sentence], cur_sent: Sentence) -> Sentence:
        labeler = Labeler()

        sentence = labeler.label(
            sentence=cur_sent, 
            prev_sentence=prev_sent, 
            get_back_link=prev_sent is not None
        )

        return sentence


    def _get_reader(self, filepath: str):
        """Fetch the reader by reading the file extension"""

        extension = filepath.split()[-1]
        reader = SUPPORTED_READERS.get(extension, None)
        if not reader:
            raise ValueError("Unsupported filetype")

        return reader()


    def build_document(self, filepath, author):
        """Build and return a fully analyzed document"""
        reader = self._get_reader(filepath)
        sentences = reader.read(filepath)
        
        prev_sentence = None
        current_sentence = None

        for sent in sentences:
            prev_sentence = current_sentence
            current_sentence = Sentence(sent)
            current_sentence = self._label_sentence(prev_sentence, current_sentence)

            sentences.append(current_sentence)
        
        doc = Document(filepath, author)
        doc.set_sentences(sentences)
        
        return doc
        
        

            

        
        



        

        
