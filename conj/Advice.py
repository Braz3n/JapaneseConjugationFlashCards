from .Word import Verb, Adjective
from .Short import conjugateShort

def formName():
    return "Recommendation/Advice"

def toolTip():
    return "Why don't you try...: 食べたらどうですか/飲んだらどうですか"

def wordGroups():
    return ["verb"]

def isTensed():
    return False

def isPolarised():
    return False

def question(word, form, tense, polarity, easy_mode, using_kanji):
    if easy_mode:
        question = "What is \"Why Don't You Try {}\"? ({})".format(word.english, word.word_to_conjugate(using_kanji))
    else:
        question = "What is \"Why Don't You Try {}\"?".format(word.english)

    answer = conjugateAdvice(word, form, tense, polarity, using_kanji)

    return question, answer

def conjugateAdvice(word, form, tense, polarity, using_kanji=False):
    if isinstance(word, Verb):
        return __verb(word, using_kanji)
    else:
        raise ValueError("Unexpected word class")

def __verb(word, using_kanji):
    ta_form = conjugateShort(word, None, "past", "affirmative", using_kanji)

    advice_form = ta_form + "らどうですか"

    return advice_form
