
class Verb():
    u_stem_dict = {'す': 'し', 'く': 'き', 'ぐ': 'ぎ', 'ぶ': 'び', 'む': 'み', 'ぬ': 'に', 'る': 'り', 'つ': 'ち', 'う': 'い'}
    u_short_dict = {'す': 'さ', 'く': 'か', 'ぐ': 'が', 'ぶ': 'ば', 'む': 'ま', 'ぬ': 'な', 'る': 'ら', 'つ': 'た', 'う': 'わ'}

    def __init__(self, verb, verb_class, english_meaning, conjugate_as=None):
        self.verb = verb
        self.verb_class = verb_class
        self.english = english_meaning
        # If the verb is a compound verb with an irregular verb.
        if conjugate_as is None:
            self.conjugate_as = verb
        else:
            self.conjugate_as = conjugate_as

    def __str__(self):
        return "{0}: {1}".format(self.verb, self.english)

    def __repr__(self):
        return "{0}: {1}".format(self.verb, self.english)

    def conjugate(self, tense, polarity, form):
        """
        tense: Either "past" or "present" Tense.
        polarity: Either "affirmative" or "negative".
        form: Either "polite" or "te" form.
        """
        if form == "te":
            conjugate = self.__te_form()
        elif form == "long":
            conjugate = self.__polite_form(tense, polarity)
        elif form == "short":
            conjugate = self.__short_form(tense, polarity)
        else:
            raise ValueError("Unexpected Verb Form Requested.\nTense: {0}\nPolarity: {1}\nForm: {2}\n".format(tense, polarity, form))

        if self.conjugate_as != self.verb:
            # If we're conjugating a compound verb, then remove the secondary verb
            # (conjugate_as) from the end of the full verb and then add the
            # conjugated secondary verb onto the end.
            conjugate = self.verb[:-len(self.conjugate_as)] + conjugate

        return conjugate

    def __te_form(self):
        if self.verb_class == "る":
            return self.__verb_stem() + "て"
        elif self.verb_class == "irregular":
            if self.conjugate_as[-2:] == "する" or self.conjugate_as[-2:] == "くる":
                return self.__verb_stem() + "て"
            else:
                raise ValueError("Unexpected Irregular Verb: {0}: {1}".format(self.verb, self.english))
        elif self.conjugate_as == "いく":
            return "いって"
        elif self.conjugate_as[-1] in "うつる":
            return self.__verb_stem()[:-1] + "って"
        elif self.conjugate_as[-1] in "むぬぶ":
            return self.__verb_stem()[:-1] + "んで"
        elif self.conjugate_as[-1] in "く":
            return self.__verb_stem()[:-1] + "いて"
        elif self.conjugate_as[-1] in "ぐ":
            return self.__verb_stem()[:-1] + "いで"
        elif self.conjugate_as[-1] in "す":
            return self.__verb_stem()[:-1] + "して"
        else:
            raise ValueError("Unexpected Verb Ending for て Form: {0}: {1}".format(self.verb, self.english))

    def __polite_form(self, tense, polarity):
        if tense == "present" and polarity == "affirmative":
            return self.__verb_stem() + "ます"
        elif tense == "present" and polarity == "negative":
            return self.__verb_stem() + "ません"
        elif tense == "past" and polarity == "affirmative":
            return self.__verb_stem() + "ました"
        elif tense == "past" and polarity == "negative":
            return self.__verb_stem() + "ませんでした"

    def __short_form(self, tense, polarity):
        if tense == "present" and polarity == "affirmative":
            return self.verb
        elif tense == "present" and polarity == "negative":
            if self.conjugate_as == 'ある' and self.verb_class == 'う':
                return 'ない'
            elif self.verb_class == 'う':
                return self.conjugate_as[:-1] + self.u_short_dict[self.conjugate_as[-1]] + "ない"
            elif self.verb_class == 'る':
                return self.conjugate_as[:-1] + "ない"
            elif self.verb_class == 'irregular':
                if self.conjugate_as[-2:] == 'する':
                    return self.__verb_stem() + 'ない'
                elif self.conjugate_as[-2:] == 'くる':
                    return self.conjugate_as[:-2] + 'こない'
                else:
                    raise ValueError("Unexpected Irregular Verb: {0}: {1}".format(self.verb, self.english))
            else:
                raise ValueError("Unexpected Verb Class: {0}: {1}".format(self.verb, self.english))
        elif tense == "past" and polarity == "affirmative":
            temp = self.__te_form()
            if temp[-1] == "て":
                return temp[:-1] + "た"
            else:
                return temp[:-1] + "だ"
        elif tense == "past" and polarity == "negative":
            return self.__short_form("present", "negative")[:-1] + "かった"

    def __verb_stem(self):
        if self.verb_class == 'う':
            verb_stem = self.conjugate_as[:-1] + self.u_stem_dict[self.conjugate_as[-1]]
        elif self.verb_class == 'る':
            verb_stem = self.conjugate_as[:-1]
        elif self.verb_class == 'irregular':
            if self.conjugate_as[-2:] == 'する':
                verb_stem = self.conjugate_as[:-2] + 'し'
            elif self.conjugate_as[-2:] == 'くる':
                verb_stem = 'き'
            else:
                raise ValueError("Unknown Irregular Verb: {0}: {1}".format(self.verb, self.english))
        return verb_stem
