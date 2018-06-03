from .Word import Verb, Adjective
from .Long import conjugateLong
from .Short import conjugateShort

def formName():
    return "Passive"

def toolTip():
    return "Passive Form: 食べられる/飲まれる"

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
        question = "What is the {}, {}, {}, passive form of \"{}\"? ({})".format(formality, tense, polarity, word.english, word.word_to_conjugate(using_kanji))
    else:
        question = "What is the {}, {}, {}, passive form of \"{}\"?".format(formality, tense, polarity, word.english)

    answer = conjugatePassive(word, formality, tense, polarity, using_kanji)

    return question, answer

def conjugatePassive(word, formality, tense, polarity, using_kanji=False):
    if isinstance(word, Verb):
        return __verb(word, formality, tense, polarity, using_kanji)
    else:
        raise ValueError("Unexpected word class")

def __verb(word, formality, tense, polarity, using_kanji):
    if using_kanji and word.kanji is not None:
        dict_form = word.kanji
    else:
        dict_form = word.kana

    if word.group == "る":
        passive_form = word.stem(using_kanji) + "られる"
    elif word.group == "う":
        passive_form = conjugateShort(word, None, "present", "negative", using_kanji)[:-1] + "れる"
    elif word.group == "irregular":
        if dict_form[-2:] == "する":
            passive_form = word.stem(using_kanji)[:-1] + "される"
        elif dict_form[-2:] == "くる":
            passive_form = word.stem(using_kanji)[:-1] + "こられる"
        elif dict_form[-2:] == "来る":
            passive_form = word.stem(using_kanji) + "来られる"

    # Create a temporary verb object so we can generate the conjugation as if
    # it were a る verb.
    if using_kanji:
        temp_verb = Verb(None, passive_form, None, "る")
    else:
        temp_verb = Verb(passive_form, None, None, "る")

    if formality == "casual" and tense == "present" and polarity == "affirmative":
        pass
    elif formality == "casual":
        passive_form = conjugateShort(temp_verb, None, tense, polarity, using_kanji)
    elif formality == "polite":
        passive_form = conjugateLong(temp_verb, None, tense, polarity, using_kanji)
    else:
        raise ValueError("Invalid form value for potential conjugation: {}".format(form))

    return passive_form
