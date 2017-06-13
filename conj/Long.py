from .Word import Verb, Adjective

def formName():
    return "Long"

def toolTip():
    return "Long Form: たべます/飲みます"

def wordGroups():
    return ["verb", "adjective"]

def isTensed():
    return True

def isPolarised():
    return True

def question(word, form, tense, polarity, easy_mode, using_kanji):
    if easy_mode:
        question = "What is the long, {}, {} form of \"{}\"? ({})".format(tense, polarity, word.english, word.word_to_conjugate(using_kanji))
    else:
        question = "What is the long, {}, {} form of \"{}\"?".format(tense, polarity, word.english)

    answer = conjugateLong(word, form, tense, polarity, using_kanji)

    return question, answer

def conjugateLong(word, form, tense, polarity, using_kanji=False):
    if isinstance(word, Verb):
        return __verb(word, tense, polarity, using_kanji)
    elif isinstance(word, Adjective):
        return __adjective(word, tense, polarity, using_kanji)
    else:
        raise ValueError("Unexpected word class")

def __verb(word, tense, polarity, using_kanji):
    stem = word.stem(using_kanji)

    if tense == "present" and polarity == "affirmative":
        long_form = stem + "ます"
    elif tense == "present" and polarity == "negative":
        long_form = stem + "ません"
    elif tense == "past" and polarity == "affirmative":
        long_form = stem + "ました"
    elif tense == "past" and polarity == "negative":
        long_form = stem + "ませんでした"

    return long_form

def __adjective(word, tense, polarity, using_kanji):
    if word.group == "い" or word.group == "いい":
        if tense == "present" and polarity == "affirmative":
            long_form = word.word_to_conjugate(using_kanji) + "です"
        elif tense == "present" and polarity == "negative":
            long_form = word.stem(using_kanji) + "くないです"
        elif tense == "past" and polarity == "affirmative":
            long_form = word.stem(using_kanji) + "かったです"
        elif tense == "past" and polarity == "negative":
            long_form = word.stem(using_kanji) + "くなかったです"
    elif word.group == "な":
        if tense == "present" and polarity == "affirmative":
            long_form = word.word_to_conjugate(using_kanji) + "です"
        elif tense == "present" and polarity == "negative":
            long_form = word.stem(using_kanji) + "じゃないです"
        elif tense == "past" and polarity == "affirmative":
            long_form = word.stem(using_kanji) + "でした"
        elif tense == "past" and polarity == "negative":
            long_form = word.stem(using_kanji) + "じゃないでした"

    return long_form
