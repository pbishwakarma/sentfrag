from sentfrag.infra.builders import DocumentBuilder

import pytest

DOC_TEXT = "Test document.\n\nNew paragraph"

@pytest.fixture(scope="module")
def db():
    doc_builder = DocumentBuilder()
    return doc_builder

def test_build_document(db):
    doc = db.build_document(DOC_TEXT)
    assert doc
    assert len(doc.get_paragraphs()) == 2
    
        

