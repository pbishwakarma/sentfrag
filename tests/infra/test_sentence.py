from sentfrag.infra.document import Sentence
from sentfrag.infra.constants import BACKWARDS_LINK, SUBJECT, VERB, LABEL_VALUE, LABEL_INDEX, LABEL_LEN

import pytest


@pytest.fixture
def sentence():
    text = "The restaurant is open for business"
    return Sentence(text)

def test_sentence_init():
    text = "Test sentence"
    sent = Sentence(text)
    
    assert text == sent.get_raw()

def test_set_label(sentence):
    label_val = "The restaurant"

    sentence.set_label(SUBJECT, label_val)
    
    labels = sentence._labels
    assert label_val == labels[SUBJECT][LABEL_VALUE]
    assert len(label_val) == labels[SUBJECT][LABEL_LEN]
    assert 0 == labels[SUBJECT][LABEL_INDEX]

def test_get_label(sentence):
    
    label_val = "The restaurant"

    labels = {
        SUBJECT: {
            LABEL_INDEX: 0,
            LABEL_VALUE: "The restaurant",
            LABEL_LEN: len(label_val)
        },
        VERB: {},
        SUBJECT: {},
        BACKWARDS_LINK: {}
    }    

    sentence._labels = labels

    assert labels == sentence.get_labels()
    
    