from sentfrag.infra.document import Document, Paragraph
    
def test_document_score_getter():
    doc = Document()
    assert doc.score == 0

def test_document_score_setter():
    doc = Document()
    doc.score = 100
    assert doc.score == 100

def test_paragraph_setter():
    doc = Document()
    p = Paragraph("Test sentence 1. Test sentence 2")
    doc.set_paragraphs([p])
    assert doc._paragraphs == [p]
    

def test_paragraph_getter():
    doc = Document()
    p = Paragraph("Test sentence 1. Test sentence 2")
    doc.set_paragraphs([p])
    assert doc.get_paragraphs() == [p]


