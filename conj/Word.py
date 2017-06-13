class Word(object):
    def __init__(self, kana, kanji, english, group):
        self.kana = kana
        self.kanji = kanji
        self.english = english
        self.group = group

    def __str__(self):
        return "<{}/{}: {}>".format(self.kana, self.kanji, self.english)

    def __repr__(self):
        return "<{}/{}: {}>".format(self.kana, self.kanji, self.english)

    def word_to_conjugate(self, using_kanji):
        # Return the Kanji form of a word if it is desired and available,
        # otherwise return the hiragana form.
        if using_kanji and self.kanji is not None:
            return self.kanji
        else:
            return self.kana

class Adjective(Word):
    def __init__(self, kana, kanji, english, group):
        super().__init__(kana, kanji, english, group)
        if group not in ["い", "な", "いい"]:
            raise ValueError("Invalid group variable for adjectve.")

    def stem(self, using_kanji):
        if self.group == "いい":
            stem = self.word_to_conjugate(using_kanji)[:-2] + "よ"
        elif self.group == "な":
            stem = self.word_to_conjugate(using_kanji)
        elif self.group == "い":
            stem = self.word_to_conjugate(using_kanji)[:-1]

        return stem

class Verb(Word):
    u_stem_dict = {'す': 'し', 'く': 'き', 'ぐ': 'ぎ', 'ぶ': 'び', 'む': 'み', 'ぬ': 'に', 'る': 'り', 'つ': 'ち', 'う': 'い'}

    def __init__(self, kana, kanji, english, group):
        super().__init__(kana, kanji, english, group)
        if group not in ["る", "う", "irregular"]:
            raise ValueError("Invalid group variable for verb.")

    def stem(self, using_kanji):
        dict_form = self.word_to_conjugate(using_kanji)

        if self.group == "る":
            stem = dict_form[:-1]
        elif self.group == "う":
            stem = dict_form[:-1] + self.u_stem_dict[dict_form[-1]]
        elif self.group == "irregular":
            if dict_form[-2:] == "する":
                stem = dict_form[:-2] + "し"
            elif dict_form[-2:] == "くる":
                stem = dict_form[:-2] + "き"
            elif dict_form[-2:] == "来る":
                stem = dict_form[:-1]
            else:
                raise ValueError("Unexpected Irregular Verb")
        else:
            raise ValueError("Unexpected Verb Group Verb")

        return stem
