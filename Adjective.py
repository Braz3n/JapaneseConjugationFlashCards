
class Adjective():
    def __init__(self, adjective, adjective_class, english_meaning, conjugate_as=None):
        self.adj = adjective
        self.adj_class = adjective_class
        self.english = english_meaning
        # If the adjective is a compound adjective with an irregular adjective,
        # we need to conjugate it as the last adjective on its own.
        # For example, the difference between かわいい and かっこいい.
        if conjugate_as is None:
            self.conjugate_as = adjective
        else:
            self.conjugate_as = conjugate_as

    def __str__(self):
        return "{0}: {1}".format(self.adj, self.english)

    def __repr__(self):
        return "{0}: {1}".format(self.adj, self.english)

    def conjugate(self, tense, polarity, form):
        """
        tense: Either "past" or "present" Tense.
        polarity: Either "positive" or "negative".
        form: Either "long" or "te" form.
        """
        if form == "te":
            conjugate = self.__te_form()
        elif form == "long":
            conjugate = self.__long_form(tense, polarity)
        elif form == "short":
            conjugate = self.__short_form(tense, polarity)
        else:
            raise ValueError("Unexpected Adjective Form Requested\nTense: {0}\nPolarity: {1}\nForm: {2}\n".format(tense, polarity, form))

        if self.conjugate_as != self.adj:
            # If we're conjugating a compound verb, then remove the secondary verb
            # (conjugate_as) from the end of the full verb and then add the
            # conjugated secondary verb onto the end.
            conjugate = self.adj[:-len(self.conjugate_as)] + conjugate

        return conjugate

    def __te_form(self):
        if self.adj_class == "な":
            return self.__adj_stem() + "で"
        elif self.adj_class == "い":
            return self.__adj_stem() + "くて"
        else:
            raise ValueError("Unexpected Adjective Class for adjective")

    def __long_form(self, tense, polarity):
        if self.adj_class == "い":
            if tense == "present" and polarity == "positive":
                return self.conjugate_as + "です"
            elif tense == "present" and polarity == "negative":
                return self.__adj_stem() + "くないです"
            elif tense == "past" and polarity == "positive":
                return self.__adj_stem() + "かったでした"
            elif tense == "past" and polarity == "negative":
                return self.__adj_stem() + "くなかったでした"
        elif self.adj_class == "な":
            if tense == "present" and polarity == "positive":
                return self.conjugate_as + "です"
            elif tense == "present" and polarity == "negative":
                return self.__adj_stem() + "じゃないです"
            elif tense == "past" and polarity == "positive":
                return self.__adj_stem() + "でした"
            elif tense == "past" and polarity == "negative":
                return self.__adj_stem() + "じゃなかったでした"

    def __short_form(self, tense, polarity):
        if self.adj_class == "い":
            if tense == "present" and polarity == "positive":
                return self.conjugate_as
            elif tense == "present" and polarity == "negative":
                return self.__adj_stem() + "くない"
            else:
                raise NotImplementedError("Wait Till Next Week!")
        elif self.adj_class == "な":
            if tense == "present" and polarity == "positive":
                return self.conjugate_as + "だ"
            elif tense == "present" and polarity == "negative":
                return self.__adj_stem() + "じゃない"
            else:
                raise NotImplementedError("Wait Till Next Week!")

    def __adj_stem(self):
        if self.conjugate_as == "いい":
            adj_stem = "よ"
        elif self.adj_class == 'な':
            adj_stem = self.conjugate_as
        elif self.adj_class == 'い':
            adj_stem = self.conjugate_as[:-1]
        return adj_stem
