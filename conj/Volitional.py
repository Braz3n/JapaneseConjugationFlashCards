from .Word import Verb, Adjective
from .Te import conjugateTe

u_volitional_dict = {'す': 'そ', 'く': 'こ', 'ぐ': 'ご', 'ぶ': 'ぼ', 'む': 'も', 'ぬ': 'の', 'る': 'ろ', 'つ': 'と', 'う': 'お'}

def formName():
    return "Volitional"

def toolTip():
    return "Volitional Form: 食べよう/飲もう"

def wordGroups():
    return ["verb"]

def hasFormalities():
    return False

def isTensed():
    return False

def isPolarised():
    return False

def question(word, formality, tense, polarity, easy_mode, using_kanji):
    if easy_mode:
        question = "What is the volitional form of \"{}\"? ({})".format(word.english, word.word_to_conjugate(using_kanji))
    else:
        question = "What is the volitional form of \"{}\"?".format(word.english)

    answer = conjugateVolitional(word, formality, tense, polarity, using_kanji)

    return question, answer

def conjugateVolitional(word, formality, tense, polarity, using_kanji=False):
    if isinstance(word, Verb):
        return __verb(word, tense, polarity, using_kanji)
    else:
        raise ValueError("Unexpected word class")

def __verb(word, tense, polarity, using_kanji):
    short_form = word.word_to_conjugate(using_kanji)

    if word.group == "う":
        volitional_form = short_form[:-1] + u_volitional_dict[short_form[-1]] + "う"
    elif word.group == "る":
        volitional_form = short_form[:-1] + "よう"
    elif word.group == "irregular":
        if short_form[-2:] == "する":
            volitional_form = short_form[:-2] + "しよう"
        elif short_form[-2:] == "くる":
            # This seems weird, but it is important for compound verbs.
            volitional_form = short_form[:-2] + "こよう"
        elif short_form[-2:] == "来る":
            volitional_form = short_form[:-1] + "よう"

    return volitional_form
