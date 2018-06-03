from .Word import Verb

def formName():
    return "To Want"

def toolTip():
    return "To Want To Do: 食べたい/飲みたい"

def wordGroups():
    return ["verb"]

def hasFormalities():
    return True

def isTensed():
    return True

def isPolarised():
    return True

def question(word, formality, tense, polarity, easy_mode, using_kanji):
    if easy_mode:
        question = "What is the {}, {}, {} form of \"To Want {}\"? ({})".format(formality, tense, polarity, word.english, word.word_to_conjugate(using_kanji))
    else:
        question = "What is the {}, {}, {} form of \"To Want {}\"?".format(formality, tense, polarity, word.english)

    answer = conjugateWant(word, formality, tense, polarity, using_kanji)

    return question, answer

def conjugateWant(word, formality, tense, polarity, using_kanji=False):
    if isinstance(word, Verb):
        return __verb(word, formality, tense, polarity, using_kanji)
    else:
        raise ValueError("Unexpected word class")

def __verb(word, formality, tense, polarity, using_kanji):
    stem = word.stem(using_kanji)

    if tense == "present" and polarity == "affirmative":
        want_form = stem + "たい"
    elif tense == "present" and polarity == "negative":
        want_form = stem + "たくない"
    elif tense == "past" and polarity == "affirmative":
        want_form = stem + "たかった"
    elif tense == "past" and polarity == "negative":
        want_form = stem + "たくなかった"

    if formality == "polite":
        want_form += "です"
    elif formality == "casual":
        pass
    else:
        raise ValueError("Invalid formality value for \"Want\" conjugation: {}".format(formality))

    return want_form
