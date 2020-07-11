from sentfrag.infra.document import Sentence
from sentfrag.infra.constants import SUBJECT, LABEL_VALUE, LABEL_INDEX, LABEL_LEN

def test_sentence_init():
    text = "Test sentence"
    sent = Sentence(text)
    
    assert text == sent.get_raw()

def test_set_label():
    text = "The restaurant is open for business"
    label_val = "The restaurant"
    sent = Sentence(text)

    sent.set_label(SUBJECT, label_val)
    
    labels = sent._labels
    assert "The restaurant" == labels[SUBJECT][LABEL_VALUE]
    assert len(label_val) == labels[SUBJECT][LABEL_LEN]
    assert 0 == labels[SUBJECT][LABEL_INDEX]