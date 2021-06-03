from nltk import pos_tag
from nltk.chunk.regexp import RegexpChunkParser, RegexpChunkRule
from nltk.tokenize import word_tokenize

import tensorflow_hub as hub


#"https://tfhub.dev/google/universal-sentence-encoder-large/5"]
#TODO: replace this with TF2 saved models
MODULE_URL = "https://tfhub.dev/google/universal-sentence-encoder/4" 

def init_model():
    model = hub.load(MODULE_URL)
    return model

def tokenize(sentence):
    """
    Split the sentence's raw text into word tokens
    """
    if not isinstance(sentence, str) or len(sentence) == 0:
        raise ValueError("Input must be a non-empty string")
    
    return word_tokenize(sentence)

def tag(sentence):
    """
    Tag each word in the tokenized sentence with part of speech
    """
    if not isinstance(sentence, list) or len(sentence) == 0:
        raise ValueError("Input must be a non empty list of strings")

    return pos_tag(sentence)

def chunk(sentence):
    """
    Group words tokens into semantic chunks (e.g. phrases)
    """
    if not isinstance(sentence, list) or len(sentence) == 0:
        raise ValueError("Input must be a non empty list of pos tagged strings")
    
    # TODO: expand this to cover more combinations
    grammar = '{<DT|PRP.*>?<NN.*>+}'
    rule = RegexpChunkRule.fromstring(grammar)
    parser = RegexpChunkParser([rule])
    return parser.parse(sentence)

def embed(model, text):
    """
    Creates an embedding of the provided text using google's universal
    sentence encoder.
    """

    return model(text)

