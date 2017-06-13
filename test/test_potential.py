import unittest
import conj.Word as Word
import conj.Potential as Potential

class TestPotential(unittest.TestCase):
    def setUp(self):
        self.verb_ru = Word.Verb("たべる", "食べる", "To Eat", "る")

        self.verb_u = Word.Verb("かう", "買う", "To Buy", "う")
        self.verb_su = Word.Verb("はなす", "話す", "To Speak", "う")
        self.verb_ku = Word.Verb("きく", "聞く", "To Listen", "う")
        self.verb_gu = Word.Verb("およぐ", "泳ぐ", "To Swim", "う")
        self.verb_bu = Word.Verb("あそぶ", "遊ぶ", "To Play", "う")
        self.verb_mu = Word.Verb("のむ", "飲む", "To Drink", "う")
        self.verb_nu = Word.Verb("しぬ", "死ぬ", "To Die", "う")
        self.verb_uru = Word.Verb("かえる", "帰る", "To Return", "う")
        self.verb_tsu = Word.Verb("もつ", "持つ", "To Hold/Carry", "う")
        self.verb_iku = Word.Verb("いく", "行く", "To Go", "う")

        self.verb_suru = Word.Verb("する", None, "To Listen", "irregular")
        self.verb_kuru = Word.Verb("くる", "来る", "To Listen", "irregular")
        self.verb_suru_compound = Word.Verb("べんきょうする", "勉強する", "To Study", "irregular")
        self.verb_kuru_compound = Word.Verb("もってくる", "持って来る", "To Bring", "irregular")

    def testVerbPotentialShortPresentAffirmative(self):
        # Only need to test short, present, positive form, since the rest
        # rely on the る conjugation code of the other forms.
        self.assertEqual(Potential.conjugatePotential(self.verb_ru, "short", "present", "affirmative", False), "たべられる")
        self.assertEqual(Potential.conjugatePotential(self.verb_ru, "short", "present", "affirmative", True), "食べられる")

        self.assertEqual(Potential.conjugatePotential(self.verb_u, "short", "present", "affirmative", False), "かえる")
        self.assertEqual(Potential.conjugatePotential(self.verb_u, "short", "present", "affirmative", True), "買える")

        self.assertEqual(Potential.conjugatePotential(self.verb_su, "short", "present", "affirmative", False), "はなせる")
        self.assertEqual(Potential.conjugatePotential(self.verb_su, "short", "present", "affirmative", True), "話せる")

        self.assertEqual(Potential.conjugatePotential(self.verb_ku, "short", "present", "affirmative", False), "きける")
        self.assertEqual(Potential.conjugatePotential(self.verb_ku, "short", "present", "affirmative", True), "聞ける")

        self.assertEqual(Potential.conjugatePotential(self.verb_gu, "short", "present", "affirmative", False), "およげる")
        self.assertEqual(Potential.conjugatePotential(self.verb_gu, "short", "present", "affirmative", True), "泳げる")

        self.assertEqual(Potential.conjugatePotential(self.verb_bu, "short", "present", "affirmative", False), "あそべる")
        self.assertEqual(Potential.conjugatePotential(self.verb_bu, "short", "present", "affirmative", True), "遊べる")

        self.assertEqual(Potential.conjugatePotential(self.verb_mu, "short", "present", "affirmative", False), "のめる")
        self.assertEqual(Potential.conjugatePotential(self.verb_mu, "short", "present", "affirmative", True), "飲める")

        self.assertEqual(Potential.conjugatePotential(self.verb_nu, "short", "present", "affirmative", False), "しねる")
        self.assertEqual(Potential.conjugatePotential(self.verb_nu, "short", "present", "affirmative", True), "死ねる")

        self.assertEqual(Potential.conjugatePotential(self.verb_uru, "short", "present", "affirmative", False), "かえれる")
        self.assertEqual(Potential.conjugatePotential(self.verb_uru, "short", "present", "affirmative", True), "帰れる")

        self.assertEqual(Potential.conjugatePotential(self.verb_tsu, "short", "present", "affirmative", False), "もてる")
        self.assertEqual(Potential.conjugatePotential(self.verb_tsu, "short", "present", "affirmative", True), "持てる")

        self.assertEqual(Potential.conjugatePotential(self.verb_iku, "short", "present", "affirmative", False), "いける")
        self.assertEqual(Potential.conjugatePotential(self.verb_iku, "short", "present", "affirmative", True), "行ける")

        self.assertEqual(Potential.conjugatePotential(self.verb_suru, "short", "present", "affirmative", False), "できる")
        self.assertEqual(Potential.conjugatePotential(self.verb_suru, "short", "present", "affirmative", True), "できる")

        self.assertEqual(Potential.conjugatePotential(self.verb_kuru, "short", "present", "affirmative", False), "こられる")
        self.assertEqual(Potential.conjugatePotential(self.verb_kuru, "short", "present", "affirmative", True), "来られる")

        self.assertEqual(Potential.conjugatePotential(self.verb_suru_compound, "short", "present", "affirmative", False), "べんきょうできる")
        self.assertEqual(Potential.conjugatePotential(self.verb_suru_compound, "short", "present", "affirmative", True), "勉強できる")

        self.assertEqual(Potential.conjugatePotential(self.verb_kuru_compound, "short", "present", "affirmative", False), "もってこられる")
        self.assertEqual(Potential.conjugatePotential(self.verb_kuru_compound, "short", "present", "affirmative", True), "持って来られる")


if __name__ == "__main__":
    unittest.main()
