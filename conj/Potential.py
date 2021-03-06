from .Word import Verb, Adjective
from .Long import conjugateLong
from .Short import conjugateShort
from .Te import conjugateTe

u_potential_dict = {'す': 'せ', 'く': 'け', 'ぐ': 'げ', 'ぶ': 'べ', 'む': 'め', 'ぬ': 'ね', 'る': 'れ', 'つ': 'て', 'う': 'え'}

def formName():
    return "Potential"

def toolTip():
    return "Potential Form: 食べられる/飲める"

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
        question = "What is the {}, {}, {}, potential form of \"{}\"? ({})".format(formality, tense, polarity, word.english, word.word_to_conjugate(using_kanji))
    else:
        question = "What is the {}, {}, {}, potential form of \"{}\"?".format(formality, tense, polarity, word.english)

    answer = conjugatePotential(word, formality, tense, polarity, using_kanji)

    return question, answer

def conjugatePotential(word, formality, tense, polarity, using_kanji=False):
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
        potential_form = word.stem(using_kanji) + "られる"
    elif word.group == "う":
        potential_form = dict_form[:-1] + u_potential_dict[dict_form[-1]] + "る"
    elif word.group == "irregular":
        if dict_form[-2:] == "する":
            potential_form = word.stem(using_kanji)[:-1] + "できる"
        elif dict_form[-2:] == "くる":
            potential_form = word.stem(using_kanji)[:-1] + "こられる"
        elif dict_form[-2:] == "来る":
            potential_form = word.stem(using_kanji) + "られる"

    # Create a temporary verb object so we can generate the conjugation as if
    # it were a る verb.
    if using_kanji:
        temp_verb = Verb(None, potential_form, None, "る")
    else:
        temp_verb = Verb(potential_form, None, None, "る")

    if formality == "casual" and tense == "present" and polarity == "affirmative":
        pass
    elif formality == "casual":
        potential_form = conjugateShort(temp_verb, None, tense, polarity, using_kanji)
    elif formality == "polite":
        potential_form = conjugateLong(temp_verb, None, tense, polarity, using_kanji)
    else:
        raise ValueError("Invalid form value for potential conjugation: {}".format(form))

    return potential_form
