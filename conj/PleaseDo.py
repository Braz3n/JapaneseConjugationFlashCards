from .Word import Verb, Adjective
from .Te import conjugateTe
from .Short import conjugateShort

def formName():
    return "Please Do/Do Not"

def toolTip():
    return "Please do/do not do something: 食べてください/食べないでください: "

def wordGroups():
    return ["verb"]

def hasFormalities():
    return False

def isTensed():
    return False

def isPolarised():
    return True

def question(word, formality, tense, polarity, easy_mode, using_kanji):
    if polarity == "affirmative":
        if easy_mode:
            question = "What is \"Please {}\"? ({})".format(word.english[3:], word.word_to_conjugate(using_kanji))
        else:
            question = "What is \"Please {}\"?".format(word.english[3:])
    else:
        if easy_mode:
            question = "What is \"Please Do Not {}\"? ({})".format(word.english[3:], word.word_to_conjugate(using_kanji))
        else:
            question = "What is \"Please Do Not {}\"?".format(word.english[3:])

    answer = conjugatePleaseDo(word, formality, tense, polarity, using_kanji)

    return question, answer

def conjugatePleaseDo(word, formality, tense, polarity, using_kanji=False):
    if isinstance(word, Verb):
        return __verb(word, polarity, using_kanji)
    else:
        raise ValueError("Unexpected word class")

def __verb(word, polarity, using_kanji):
    if polarity == "affirmative":
        please = conjugateTe(word, None, None, None, using_kanji) + "ください"
    elif polarity == "negative":
        please = conjugateShort(word, None, "present", "negative", using_kanji) + "でください"

    return please
