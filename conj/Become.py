from .Word import Verb, Adjective
from .Short import conjugateShort
from .Long import conjugateLong

def formName():
    return "To Become"

def toolTip():
    return "To Become: あつくなる/げんきになる"

def wordGroups():
    return ["adjective"]

def isTensed():
    return True

def isPolarised():
    return True

def question(word, form, tense, polarity, easy_mode, using_kanji):
    if form not in ["long", "short"]:
        form = "short"
    if easy_mode:
        question = "What is the {}, {}, {} form of \"To Become {}\"? ({})".format(form, tense, polarity, word.english, word.word_to_conjugate(using_kanji))
    else:
        question = "What is the {}, {}, {} form of \"To Become {}\"?".format(form, tense, polarity, word.english)

    answer = conjugateBecome(word, form, tense, polarity, using_kanji)

    return question, answer

def conjugateBecome(word, form, tense, polarity, using_kanji=False):
    if isinstance(word, Adjective):
        return __adjective(word, form, tense, polarity, using_kanji)
    else:
        raise ValueError("Unexpected word class")

def __adjective(word, form, tense, polarity, using_kanji):
    naru = Verb("なる", "成る", "To Become", "う")
    if form == "short":
        naru = conjugateShort(naru, None, tense, polarity)
    elif form == "long":
        naru = conjugateLong(naru, None, tense, polarity)
    else:
        raise ValueError("Invalid form value for \"Become\" conjugation: {}".format(form))

    become_form = word.stem(using_kanji)
    if word.group in ["い", "いい"]:
        become_form += "く" + naru

    elif word.group == "な":
        become_form += "に" + naru

    return become_form
