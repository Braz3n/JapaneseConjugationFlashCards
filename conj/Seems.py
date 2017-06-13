from .Word import Verb, Adjective
from .Short import conjugateShort

def formName():
    return "Seems To Be"

def toolTip():
    return "To Seem Like: あつそうです/げんきそうです"

def wordGroups():
    return ["adjective"]

def isTensed():
    return True

def isPolarised():
    return True

def question(word, form, tense, polarity, easy_mode, using_kanji):
    if easy_mode:
        question = "What is the {}, {} form of \"Seems {}\"? ({})".format(form, polarity, word.english, word.word_to_conjugate(using_kanji))
    else:
        question = "What is the {}, {} form of \"Seems {}\"?".format(form, polarity, word.english)

    answer = conjugateSeems(word, form, tense, polarity, using_kanji)

    return question, answer

def conjugateSeems(word, form, tense, polarity, using_kanji=False):
    if isinstance(word, Adjective):
        return __adjective(word, tense, polarity, using_kanji)
    else:
        raise ValueError("Unexpected word class")

def __adjective(word, tense, polarity, using_kanji):
    short_form = conjugateShort(word, None, "present", polarity, using_kanji)
    if word.group == "いい" and polarity == "affirmative":
        short_form = short_form[:-2] + "よさ"
    elif word.group == "いい" and polarity == "negative":
        short_form = short_form[:-4] + "よさな"
    else:
        # Drop the final character.
        #   For い adjectives, this is the final い.
        #   For な adjectives, this is either だ or the い of じゃない if in the negative form.
        short_form = short_form[:-1]

    if tense == "past":
        seems_form = short_form + "そうでした"
    else:
        seems_form = short_form + "そうです"

    return seems_form
