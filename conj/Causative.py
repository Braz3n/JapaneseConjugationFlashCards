from .Word import Verb, Adjective
from .Long import conjugateLong
from .Short import conjugateShort

def formName():
    return "Causative"

def toolTip():
    return "Causative Form: 食べさせる/飲ませる"

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
        question = "What is the {}, {}, {}, causative form of \"{}\"? ({})".format(formality, tense, polarity, word.english, word.word_to_conjugate(using_kanji))
    else:
        question = "What is the {}, {}, {}, causative form of \"{}\"?".format(formality, tense, polarity, word.english)

    answer = conjugateCausative(word, formality, tense, polarity, using_kanji)

    return question, answer

def conjugateCausative(word, formality, tense, polarity, using_kanji=False):
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
        causative_form = word.stem(using_kanji) + "させる"
    elif word.group == "う":
        causative_form = conjugateShort(word, None, "present", "negative", using_kanji)[:-1] + "せる"
    elif word.group == "irregular":
        if dict_form[-2:] == "する":
            causative_form = word.stem(using_kanji)[:-1] + "させる"
        elif dict_form[-2:] == "くる":
            causative_form = word.stem(using_kanji)[:-1] + "こさせる"
        elif dict_form[-2:] == "来る":
            causative_form = word.stem(using_kanji) + "来させる"

    # Create a temporary verb object so we can generate the conjugation as if
    # it were a る verb.
    if using_kanji:
        temp_verb = Verb(None, causative_form, None, "る")
    else:
        temp_verb = Verb(causative_form, None, None, "る")

    if formality == "casual" and tense == "present" and polarity == "affirmative":
        pass
    elif formality == "casual":
        causative_form = conjugateShort(temp_verb, None, tense, polarity, using_kanji)
    elif formality == "polite":
        causative_form = conjugateLong(temp_verb, None, tense, polarity, using_kanji)
    else:
        raise ValueError("Invalid form value for potential conjugation: {}".format(form))

    return causative_form
