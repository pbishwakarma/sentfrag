from string import punctuation
from typing import Optional

from sentfrag.infra.document import Document, Paragraph, Sentence
from sentfrag.gopen.labeler import Labeler

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


    def build_document(self, raw):
        """Build and return a document"""
    
        doc = Document()
    
        #Split into paragraphs
        _paragraphs = raw.split("\n\n")
        paragraphs = [Paragraph(p) for p in _paragraphs]

        doc.set_paragraphs(paragraphs)
        
        return doc
        
        

            

        
        



        

        
