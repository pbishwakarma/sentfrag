from datetime import datetime

from sentfrag.infra.document import Document, Sentence, Paragraph

def test_document_filepath_prop():
    exp_filepath = "test/filepath"
    doc = Document(filepath=exp_filepath, author=None)
    assert exp_filepath == doc.filepath


def test_document_author_prop():
    exp_author = "test author"
    doc = Document(filepath=None, author=exp_author)
    assert exp_author == doc.author

def test_document_created_prop():
    doc = Document(filepath=None, author=None)
    assert doc.created != None
    
def test_document_score_getter():
    doc = Document(filepath=None, author=None)
    assert doc.score == 0

def test_document_score_setter():
    doc = Document(filepath=None, author=None)
    doc.score = 100
    assert doc.score == 100

def test_paragraph_setter():
    doc = Document(filepath=None, author=None)
    p = Paragraph("Test sentence 1. Test sentence 2")
    doc.set_paragraphs([p])
    assert doc._paragraphs == [p]
    

def test_paragraph_getter():
    doc = Document(filepath=None, author=None)
    p = Paragraph("Test sentence 1. Test sentence 2")
    doc.set_paragraphs([p])
    assert doc.get_paragraphs() == [p]


