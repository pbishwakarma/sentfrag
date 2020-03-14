from nltk.tokenize import word_tokenize
from nltk import pos_tag


def label_words(sentence):
    words = word_tokenize(sentence)
    tagged = pos_tag(words)
    print(tagged)


if __name__ == "__main__":
    print("test")
    label_words("This is the way")

