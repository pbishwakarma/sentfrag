from nltk import pos_tag
from nltk.chunk.regexp import RegexpChunkParser, RegexpChunkRule
from nltk.tokenize import word_tokenize

import tensorflow_hub as hub


#"https://tfhub.dev/google/universal-sentence-encoder-large/5"]
#TODO: load at app startup from local download
module_url = "https://tfhub.dev/google/universal-sentence-encoder/4" 
model = hub.load(module_url)
  
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

def embed(text):
    """
    Creates an embedding of the provided text using google's universal
    sentence encoder.
    """

    return model(text)

