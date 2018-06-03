from .Word import Verb, Adjective
from .Short import conjugateShort

def formName():
    return "Maybe"

def toolTip():
    return "Something is Probable: 食べるかもしれません"

def wordGroups():
    return ["verb", "adjective"]

def hasFormalities():
    return True

def isTensed():
    return True

def isPolarised():
    return True

def question(word, formality, tense, polarity, easy_mode, using_kanji):
    if isinstance(word, Verb):
        if easy_mode:
            question = "What is the {}, {}, {} form of \"I Might {}\"? ({})".format(formality, tense, polarity, word.english[3:], word.word_to_conjugate(using_kanji))
        else:
            question = "What is the {}, {}, {} form of \"I Might {}\"?".format(formality, tense, polarity, word.english[3:])
    elif isinstance(word, Adjective):
        if easy_mode:
            question = "What is the {}, {}, {} form of \"It Might Be {}\"? ({})".format(formality, tense, polarity, word.english, word.word_to_conjugate(using_kanji))
        else:
            question = "What is the {}, {}, {} form of \"It Might Be {}\"?".format(formality, tense, polarity, word.english)

    answer = conjugateMaybe(word, formality, tense, polarity, using_kanji)

    return question, answer

def conjugateMaybe(word, formality, tense, polarity, using_kanji=False):
    if isinstance(word, Verb):
        return __verb(word, formality, tense, polarity, using_kanji)
    elif isinstance(word, Adjective):
        return __adjective(word, formality, tense, polarity, using_kanji)
    else:
        raise ValueError("Unexpected word class")

def __verb(word, formality, tense, polarity, using_kanji):
    if formality == "polite":
        maybe = conjugateShort(word, None, tense, polarity) + "かもしれません"
    elif formality == "casual":
        maybe = conjugateShort(word, None, tense, polarity) + "かもしれない"
    else:
        raise ValueError("Invalid formality value for \"Maybe\" conjugation: {}".format(formality))

    return maybe

def __adjective(word, formality, tense, polarity, using_kanji):
    short_form = conjugateShort(word, None, tense, polarity)

    if word.group is "な":
        # We don't follow な-adjectives with だ in this form.
        short_form = short_form[:-1]

    if formality == "polite":
        maybe = short_form + "かもしれません"
    elif formality == "casual":
        maybe = short_form + "かもしれない"
    else:
        raise ValueError("Invalid formality value for \"Maybe\" conjugation: {}".format(formality))

    return maybe
