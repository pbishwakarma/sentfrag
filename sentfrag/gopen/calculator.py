from sentfrag.infra.document import Document, Sentence


class Calculator(object):
    """
    Calculates a score for the document based on the pos_tagging.
    """

    def __init__(self, tagset):
        self.set_tagset(tagset)
    
    def set_tagset(self, tagset):
        """
        Assigns the tags to look for while calculating the score for the document.
        Tagsets  consist of different tags that  specify components of a sentence.
        """
        
        pass

    def calculate(self, doc: Document):
        """
        Calculate the score of a document.
        """
        
        pass

    def calculate(self, sent: Sentence):
        """
        Calculates the score of a sentence
        """

        pass

