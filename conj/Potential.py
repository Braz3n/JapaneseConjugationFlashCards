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

def isTensed():
    return True

def isPolarised():
    return True

def question(word, form, tense, polarity, easy_mode, using_kanji):
    if form not in ["long", "short"]:
        # If we are only testing the potential form, it is possible to get the
        # potential form of the potential form.
        form = "short"

    if easy_mode:
        question = "What is the {}, {}, {}, potential form of \"{}\"? ({})".format(form, tense, polarity, word.english, word.word_to_conjugate(using_kanji))
    else:
        question = "What is the {}, {}, {}, potential form of \"{}\"?".format(form, tense, polarity, word.english)

    answer = conjugatePotential(word, form, tense, polarity, using_kanji)

    return question, answer

def conjugatePotential(word, form, tense, polarity, using_kanji=False):
    if isinstance(word, Verb):
        return __verb(word, form, tense, polarity, using_kanji)
    else:
        raise ValueError("Unexpected word class")

def __verb(word, form, tense, polarity, using_kanji):
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

    # TODO How are we going to do this? With a link to a function? Or from keywords?
    # What if every conjugation button linked to a function pointer?
    # For the time being, we'll assume it's one of short, long or te form.
    if form == "short" and tense == "present" and polarity == "affirmative":
        pass
    elif form == "short":
        potential_form = conjugateShort(temp_verb, None, tense, polarity, using_kanji)
    elif form == "long":
        potential_form = conjugateLong(temp_verb, None, tense, polarity, using_kanji)
    elif form == "te":
        potential_form = conjugateTe(temp_verb, None, None, None, using_kanji)
    else:
        raise ValueError("Invalid form value for potential conjugation: {}".format(form))

    return potential_form
