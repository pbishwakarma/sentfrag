from string import punctuation
from typing import Optional

from sentfrag.infra.document import Document, Paragraph, Sentence
from sentfrag.gopen.labeler import Labeler
from sentfrag.preprocessors.readers import TXTReader, SUPPORTED_READERS

from nltk import sent_tokenize

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

        extension = filepath.split(".")[-1]
        reader = SUPPORTED_READERS.get(extension, None)
        if not reader:
            raise ValueError("Unsupported filetype")

        return reader(filepath)


    def build_document(self, filepath, author):
        """Build and return a fully analyzed document"""
        reader = self._get_reader(filepath)
    
        text = reader.read()
        
        doc = Document(filepath, author)
    
        #Split into paragraphs
        _paragraphs = text.split("\n\n")
        paragraphs = [Paragraph(p) for p in _paragraphs]

        doc.set_paragraphs(paragraphs)
        
        return doc
        
        

            

        
        



        

        
