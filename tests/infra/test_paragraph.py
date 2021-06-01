from sentfrag.infra.document import Paragraph, Sentence

import pytest


def test_paragraph_init():
    text = "Test sentence 1. Test sentence 2"
    p = Paragraph(text)
    
    assert str(p) == text

def test_set_sentences():
    s = [
        Sentence("Test Sentence 1"),
        Sentence("Test Sentence 2")
    ]

    p = Paragraph("Test Sentence 1. Test Sentence 2.")
    p.set_sentences(s)
    
    for pair in zip(s, p.get_sentences()):
        assert pair[0] == pair[1]

def test_get_sentences():
    s = [
        Sentence("Test Sentence 1")
    ]

    p = Paragraph("Test Sentence 1")
    _s = p.get_sentences()

    for sent in s:
        print(sent.get_raw())
    
    for sent in _s:
        print(sent.get_raw())

    for pair in zip(s, _s):
        assert pair[0] == pair[1]
    