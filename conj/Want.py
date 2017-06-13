from .Word import Verb

def formName():
    return "To Want"

def toolTip():
    return "To Want To Do: 食べたい/飲みたい"

def wordGroups():
    return ["verb"]

def isTensed():
    return True

def isPolarised():
    return True

def question(word, form, tense, polarity, easy_mode, using_kanji):
    if form.lower() not in ["long", "short"]:
        form = "short"
    if easy_mode:
        question = "What is the {}, {}, {} form of \"To Want {}\"? ({})".format(form, tense, polarity, word.english, word.word_to_conjugate(using_kanji))
    else:
        question = "What is the {}, {}, {} form of \"To Want {}\"?".format(form, tense, polarity, word.english)

    answer = conjugateWant(word, form, tense, polarity, using_kanji)

    return question, answer

def conjugateWant(word, form, tense, polarity, using_kanji=False):
    if isinstance(word, Verb):
        return __verb(word, form, tense, polarity, using_kanji)
    else:
        raise ValueError("Unexpected word class")

def __verb(word, form, tense, polarity, using_kanji):
    stem = word.stem(using_kanji)

    if tense == "present" and polarity == "affirmative":
        want_form = stem + "たい"
    elif tense == "present" and polarity == "negative":
        want_form = stem + "たくない"
    elif tense == "past" and polarity == "affirmative":
        want_form = stem + "たかった"
    elif tense == "past" and polarity == "negative":
        want_form = stem + "たくなかった"

    if form.lower() == "long":
        want_form += "です"

    return want_form
