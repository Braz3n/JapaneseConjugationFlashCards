from .Word import Verb, Adjective

u_te_dict = {'す': 'して', 'く': 'いて', 'ぐ': 'いで', 'ぶ': 'んで', 'む': 'んで', 'ぬ': 'んで', 'る': 'って', 'つ': 'って', 'う': 'って'}

def formName():
    return "Te"

def toolTip():
    return "Te Form: 食べて/飲んで"

def wordGroups():
    return ["verb", "adjective"]

def hasFormalities():
    return False

def isTensed():
    return False

def isPolarised():
    return False

def question(word, formality, tense, polarity, easy_mode, using_kanji):
    if easy_mode:
        question = "What is the Te form of \"{}\"? ({})".format(word.english, word.word_to_conjugate(using_kanji))
    else:
        question = "What is the Te form of \"{}\"?".format(word.english)

    answer = conjugateTe(word, formality, tense, polarity, using_kanji)

    return question, answer

def conjugateTe(word, formality, tense, polarity, using_kanji=False):
    if isinstance(word, Verb):
        return __verb(word, using_kanji)
    elif isinstance(word, Adjective):
        return __adjective(word, using_kanji)
    else:
        raise ValueError("Unexpected word class")

def __verb(word, using_kanji):
    dict_form = word.word_to_conjugate(using_kanji)

    if word.group == "る" or word.group == "irregular":
        te_form = word.stem(using_kanji) + "て"
    elif dict_form[-2:] == "いく" or dict_form[-2:] == "行く":
        te_form = word.stem(using_kanji)[:-1] + "って"
    elif word.group == "う":
        te_form = dict_form[:-1] + u_te_dict[dict_form[-1]]

    return te_form

def __adjective(word, using_kanji):
    if word.group == "な":
        te_form = word.stem(using_kanji) + "で"
    elif word.group == "い" or word.group == "いい":
        te_form = word.stem(using_kanji) + "くて"

    return te_form
