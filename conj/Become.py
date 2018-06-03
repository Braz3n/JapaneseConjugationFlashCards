from .Word import Verb, Adjective
from .Short import conjugateShort
from .Long import conjugateLong

def formName():
    return "To Become"

def toolTip():
    return "To Become: あつくなる/げんきになる"

def wordGroups():
    return ["adjective"]

def hasFormalities():
    return True

def isTensed():
    return True

def isPolarised():
    return True

def question(word, formality, tense, polarity, easy_mode, using_kanji):
    if easy_mode:
        question = "What is the {}, {}, {} form of \"To Become {}\"? ({})".format(formality, tense, polarity, word.english, word.word_to_conjugate(using_kanji))
    else:
        question = "What is the {}, {}, {} form of \"To Become {}\"?".format(formality, tense, polarity, word.english)

    answer = conjugateBecome(word, formality, tense, polarity, using_kanji)

    return question, answer

def conjugateBecome(word, formality, tense, polarity, using_kanji=False):
    if isinstance(word, Adjective):
        return __adjective(word, formality, tense, polarity, using_kanji)
    else:
        raise ValueError("Unexpected word class")

def __adjective(word, formality, tense, polarity, using_kanji):
    naru = Verb("なる", "成る", "To Become", "う")

    if formality == "casual":
        naru = conjugateShort(naru, None, tense, polarity)
    elif formality == "polite":
        naru = conjugateLong(naru, None, tense, polarity)
    else:
        raise ValueError("Invalid formality value for \"Become\" conjugation: {}".format(formality))

    become_form = word.stem(using_kanji)
    if word.group in ["い", "いい"]:
        become_form += "く" + naru

    elif word.group == "な":
        become_form += "に" + naru

    return become_form
