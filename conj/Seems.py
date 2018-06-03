from .Word import Verb, Adjective
from .Short import conjugateShort

def formName():
    return "Seems To Be"

def toolTip():
    return "To Seem Like: あつそうです/げんきそうです"

def wordGroups():
    return ["adjective"]

def hasFormalities():
    return True

def isTensed():
    return True

def isPolarised():
    return True

def question(word, formality, tense, polarity, easy_mode, using_kanji):
    if easy_mode:
        question = "What is the {}, {} form of \"Seems {}\"? ({})".format(formality, polarity, word.english, word.word_to_conjugate(using_kanji))
    else:
        question = "What is the {}, {} form of \"Seems {}\"?".format(formality, polarity, word.english)

    answer = conjugateSeems(word, formality, tense, polarity, using_kanji)

    return question, answer

def conjugateSeems(word, formality, tense, polarity, using_kanji=False):
    if isinstance(word, Adjective):
        return __adjective(word, formality, tense, polarity, using_kanji)
    else:
        raise ValueError("Unexpected word class")

def __adjective(word, formality, tense, polarity, using_kanji):
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

    if formality == "casual":
        if tense == "past":
            seems_form = short_form + "そうだった"
        else:
            seems_form = short_form + "そうだ"
    elif formality == "polite":
        if tense == "past":
            seems_form = short_form + "そうでした"
        else:
            seems_form = short_form + "そうです"
    else:
        raise ValueError("Invalid formality value for \"Seems\" conjugation: {}".format(formality))

    return seems_form
