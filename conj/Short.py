from .Word import Verb, Adjective
from .Te import conjugateTe

u_short_dict = {'す': 'さ', 'く': 'か', 'ぐ': 'が', 'ぶ': 'ば', 'む': 'ま', 'ぬ': 'な', 'る': 'ら', 'つ': 'た', 'う': 'わ'}

def formName():
    return "Short"

def toolTip():
    return "Short Form: 食べる/飲む"

def wordGroups():
    return ["verb", "adjective"]

def hasFormalities():
    return False

def isTensed():
    return True

def isPolarised():
    return True

def question(word, formality, tense, polarity, easy_mode, using_kanji):
    if easy_mode:
        question = "What is the short, {}, {} form of \"{}\"? ({})".format(tense, polarity, word.english, word.word_to_conjugate(using_kanji))
    else:
        question = "What is the short, {}, {} form of \"{}\"?".format(tense, polarity, word.english)

    answer = conjugateShort(word, formality, tense, polarity, using_kanji)

    return question, answer

def conjugateShort(word, formality, tense, polarity, using_kanji=False):
    if isinstance(word, Verb):
        return __verb(word, tense, polarity, using_kanji)
    elif isinstance(word, Adjective):
        return __adjective(word, tense, polarity, using_kanji)
    else:
        raise ValueError("Unexpected word class")

def __verb(word, tense, polarity, using_kanji):
    short_form = word.word_to_conjugate(using_kanji)

    if tense == "present" and polarity == "affirmative":
        pass
    elif tense == "present" and polarity == "negative":
        if (short_form[-2:] == "ある" or short_form[-2:] == "有る") and word.group == "う":
            short_form = "ない"  # Does this have a form with kanji?
        elif word.group == "う":
            short_form = short_form[:-1] + u_short_dict[short_form[-1]] + "ない"
        elif word.group == "る":
            short_form = short_form[:-1] + "ない"
        elif word.group == "irregular":
            if short_form[-2:] == "する":
                short_form = word.stem(using_kanji) + "ない"
            elif short_form[-2:] == "くる":
                # This seems weird, but it is important for compound verbs.
                short_form = short_form[:-2] + "こない"
            elif short_form[-2:] == "来る":
                short_form = short_form[:-1] + "ない"
    elif tense == "past" and polarity == "affirmative":
        short_form = conjugateTe(word, None, None, None, using_kanji)
        if short_form[-1] == "て":
            short_form = short_form[:-1] + "た"
        elif short_form[-1] == "で":
            short_form = short_form[:-1] + "だ"
    elif tense == "past" and polarity == "negative":
        short_form = __verb(word, "present", "negative", using_kanji)[:-1] + "かった"

    return short_form

def __adjective(word, tense, polarity, using_kanji):
    if word.group == "い" or word.group == "いい":
        if tense == "present" and polarity == "affirmative":
            short_form = word.word_to_conjugate(using_kanji)
        elif tense == "present" and polarity == "negative":
            short_form = word.stem(using_kanji) + "くない"
        elif tense == "past" and polarity == "affirmative":
            short_form = word.stem(using_kanji) + "かった"
        elif tense == "past" and polarity == "negative":
            short_form = word.stem(using_kanji) + "くなかった"
    elif word.group == "な":
        if tense == "present" and polarity == "affirmative":
            short_form = word.word_to_conjugate(using_kanji) + "だ"
        elif tense == "present" and polarity == "negative":
            short_form = word.word_to_conjugate(using_kanji) + "じゃない"
        elif tense == "past" and polarity == "affirmative":
            short_form = word.stem(using_kanji) + "だった"
        elif tense == "past" and polarity == "negative":
            short_form = word.stem(using_kanji) + "じゃなかった"

    return short_form
