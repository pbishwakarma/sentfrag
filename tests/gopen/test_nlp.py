import pytest

from sentfrag.infra.document import Sentence
from sentfrag.gopen.nlp import init_model, tokenize, tag, chunk, embed

from nltk.tree import Tree
from tensorflow import is_tensor

@pytest.fixture
def s1():
    return "The boy plays soccer."

@pytest.fixture(scope="module")
def m():
    return init_model()

def test_init_model():
    model = init_model()
    assert model

def test_tokenize(s1):
    tokenized = tokenize(s1)
    assert type(tokenized) == list and len(tokenized) == 5

#TODO: make the expected exception test a decorator for some syncactic sugar
def test_tokenize_empty_string():
    with pytest.raises(ValueError):
        _ = tokenize("")

def test_tokenize_non_string():
    with pytest.raises(ValueError):
        _ = tokenize(123)

def test_tag(s1):
    tokenized = tokenize(s1)
    tagged = tag(tokenized)
    assert type(tagged) == list and len(tagged) == len(tokenized)

def test_tag_non_list():
    with pytest.raises(ValueError):
        _ = tag("")

def test_tag_empty_list():
    with pytest.raises(ValueError):
        _ = tag([])

def test_chunk(s1):
    tokenized = tokenize(s1)
    tagged = tag(tokenized)
    chunked = chunk(tagged)

    assert type(chunked) == Tree and len(chunked) != 0

def test_chunk_empty_list():
    with pytest.raises(ValueError):
        _ = chunk([])

def test_chunk_non_list():
    with pytest.raises(ValueError):
        _ = chunk("")

def test_embed(s1, m):
    embedded = m([s1])
    assert is_tensor(embedded)
    
    

