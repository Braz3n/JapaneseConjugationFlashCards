from .Word import Verb, Adjective
from .Short import conjugateShort

def formName():
    return "I Hear"

def toolTip():
    return "Hearsay: ～そうです"

def wordGroups():
    return ["verb", "adjective"]

def hasFormalities():
    return True

def isTensed():
    return True

def isPolarised():
    return False

def question(word, formality, tense, polarity, easy_mode, using_kanji):
    if isinstance(word, Verb):
        if easy_mode:
            question = "What is the {}, {}, {}, form of \"I heard they {}\"? ({})".format(formality, tense, polarity, word.english[3:], word.word_to_conjugate(using_kanji))
        else:
            question = "What is the {}, {}, {}, form of \"I heard they {}\"?".format(formality, tense, polarity, word.english[3:])
    elif isinstance(word, Adjective):
        if easy_mode:
            question = "What is the {}, {}, {}, form of \"I heard it is {}\"? ({})".format(formality, tense, polarity, word.english, word.word_to_conjugate(using_kanji))
        else:
            question = "What is the {}, {}, {}, form of \"I heard it is {}\"?".format(formality, tense, polarity, word.english)

    answer = conjugateHearsay(word, formality, tense, polarity, using_kanji)

    return question, answer

def conjugateHearsay(word, formality, tense, polarity, using_kanji=False):
    if isinstance(word, Verb):
        return __verb(word, formality, tense, polarity, using_kanji)
    elif isinstance(word, Adjective):
        return __adjective(word, formality, tense, polarity, using_kanji)
    else:
        raise ValueError("Unexpected word class")

def __verb(word, formality, tense, polarity, using_kanji):
    short_form = conjugateShort(word, None, tense, polarity)

    if formality == "polite":
        hearsay = short_form + "そうです"
    elif formality == "casual":
        hearsay = short_form + "そうだ"
    else:
        raise ValueError("Invalid formality value for \"Hearsay\" conjugation: {}".format(formality))

    return hearsay

def __adjective(word, formality, tense, polarity, using_kanji):
    short_form = conjugateShort(word, None, tense, polarity)

    if formality == "polite":
        hearsay = short_form + "そうです"
    elif formality == "casual":
        hearsay = short_form + "そうだ"
    else:
        raise ValueError("Invalid formality value for \"Hearsay\" conjugation: {}".format(formality))

    return hearsay
