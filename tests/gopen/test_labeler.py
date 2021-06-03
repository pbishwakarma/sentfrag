import pytest

from sentfrag.gopen.nlp import init_model
from sentfrag.gopen.labeler import Labeler
from sentfrag.infra.builders import DocumentBuilder
from sentfrag.infra.constants import BACKWARDS_LINK, STRESS_POSITION, SUBJECT, VERB

@pytest.fixture(scope="module")
def l():
    model = init_model()
    return Labeler(model)

@pytest.fixture(scope="function")
def doc():
    db = DocumentBuilder()
    return db.build_document("tests/data/test_doc.txt", "test_author")

@pytest.fixture(scope="function")
def p(doc):
    return doc.get_paragraphs()[0]

@pytest.fixture(scope="function")
def s(p):
    return p.get_sentences()[0]

@pytest.fixture(scope="function")
def s2(p):
    return p.get_sentences()[1]

@pytest.fixture(scope="function")
def chunked_s(s, l):
    l._label(s)
    return s

@pytest.fixture(scope="function")
def chunked_s2(s2, l):
    l._label(s2)
    return s2

def test_private_label(l, s):
    assert not s.get_tokenized()
    assert not s.get_pos()
    assert not s.get_chunks()
    l._label(s)
    assert s.get_tokenized()
    assert s.get_pos()
    assert s.get_chunks()

def test_public_label(l, s):
    labeled_s = l.label(s, None, False)
    assert labeled_s.get_tokenized()
    assert labeled_s.get_pos()
    assert labeled_s.get_chunks()

    for k, v in labeled_s.get_labels().items():
        if k == BACKWARDS_LINK:
            assert not v
        else:
            assert v

def test_public_label_chunked(l, chunked_s):
    labeled_s = l.label(chunked_s, None, False)
    
    for k, v in labeled_s.get_labels().items():
        if k == BACKWARDS_LINK:
            assert not v
        else:
            assert v

def test_get_subject(l, chunked_s):
    subject = l.get_subject(chunked_s)
    assert subject

def test_get_verb(l, chunked_s):
    verb = l.get_verb(chunked_s)
    assert verb

def test_get_stress_position(l, chunked_s):
    sp = l.get_stress_position(chunked_s)
    assert sp

def test_get_backward_link(l, chunked_s, chunked_s2):
    bl = l.get_backward_link(chunked_s2, chunked_s)
    assert bl

def test_label_paragraph(l, p):
    for s in p.get_sentences():
        assert not s.get_chunks()

    labeled_p = l.label_paragraph(p)
    for s in labeled_p.get_sentences():
        assert s.get_chunks()

def test_label_document(l, doc):
    for p in doc.get_paragraphs():
        for s in p.get_sentences():
            assert not s.get_chunks()

    labeled_doc = l.label_document(doc)

    for p in labeled_doc.get_paragraphs():
        for s in p.get_sentences():
            assert s.get_chunks()
    
          
    