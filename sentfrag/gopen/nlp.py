from nltk import pos_tag
from nltk.chunk.regexp import RegexpChunkParser, RegexpChunkRule
from nltk.tokenize import word_tokenize

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

