import unittest
import conj.Word as Word
import conj.Te as Te

class TestTe(unittest.TestCase):
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

        self.adj_i = Word.Adjective("かわいい", None, "Cute", "い")
        self.adj_ii = Word.Adjective("いい", None, "Good", "いい")
        self.adj_ii_compound = Word.Adjective("かっこいい", None, "Cool", "いい")
        self.adj_na = Word.Adjective("げんき", "元気", "Healthy/Energetic", "な")

    def testVerbTe(self):
        self.assertEqual(Te.conjugateTe(self.verb_ru, None, None, None, False), "たべて")
        self.assertEqual(Te.conjugateTe(self.verb_ru, None, None, None, True), "食べて")

        self.assertEqual(Te.conjugateTe(self.verb_u, None, None, None, False), "かって")
        self.assertEqual(Te.conjugateTe(self.verb_u, None, None, None, True), "買って")

        self.assertEqual(Te.conjugateTe(self.verb_su, None, None, None, False), "はなして")
        self.assertEqual(Te.conjugateTe(self.verb_su, None, None, None, True), "話して")

        self.assertEqual(Te.conjugateTe(self.verb_ku, None, None, None, False), "きいて")
        self.assertEqual(Te.conjugateTe(self.verb_ku, None, None, None, True), "聞いて")

        self.assertEqual(Te.conjugateTe(self.verb_gu, None, None, None, False), "およいで")
        self.assertEqual(Te.conjugateTe(self.verb_gu, None, None, None, True), "泳いで")

        self.assertEqual(Te.conjugateTe(self.verb_bu, None, None, None, False), "あそんで")
        self.assertEqual(Te.conjugateTe(self.verb_bu, None, None, None, True), "遊んで")

        self.assertEqual(Te.conjugateTe(self.verb_mu, None, None, None, False), "のんで")
        self.assertEqual(Te.conjugateTe(self.verb_mu, None, None, None, True), "飲んで")

        self.assertEqual(Te.conjugateTe(self.verb_nu, None, None, None, False), "しんで")
        self.assertEqual(Te.conjugateTe(self.verb_nu, None, None, None, True), "死んで")

        self.assertEqual(Te.conjugateTe(self.verb_uru, None, None, None, False), "かえって")
        self.assertEqual(Te.conjugateTe(self.verb_uru, None, None, None, True), "帰って")

        self.assertEqual(Te.conjugateTe(self.verb_tsu, None, None, None, False), "もって")
        self.assertEqual(Te.conjugateTe(self.verb_tsu, None, None, None, True), "持って")

        self.assertEqual(Te.conjugateTe(self.verb_iku, None, None, None, False), "いって")
        self.assertEqual(Te.conjugateTe(self.verb_iku, None, None, None, True), "行って")

        self.assertEqual(Te.conjugateTe(self.verb_suru, None, None, None, False), "して")
        self.assertEqual(Te.conjugateTe(self.verb_suru, None, None, None, True), "して")

        self.assertEqual(Te.conjugateTe(self.verb_kuru, None, None, None, False), "きて")
        self.assertEqual(Te.conjugateTe(self.verb_kuru, None, None, None, True), "来て")

        self.assertEqual(Te.conjugateTe(self.verb_suru_compound, None, None, None, False), "べんきょうして")
        self.assertEqual(Te.conjugateTe(self.verb_suru_compound, None, None, None, True), "勉強して")

        self.assertEqual(Te.conjugateTe(self.verb_kuru_compound, None, None, None, False), "もってきて")
        self.assertEqual(Te.conjugateTe(self.verb_kuru_compound, None, None, None, True), "持って来て")

    def testAdjTe(self):
        self.assertEqual(Te.conjugateTe(self.adj_i, None, None, None, False), "かわいくて")
        self.assertEqual(Te.conjugateTe(self.adj_i, None, None, None, True), "かわいくて")

        self.assertEqual(Te.conjugateTe(self.adj_ii, None, None, None, False), "よくて")
        self.assertEqual(Te.conjugateTe(self.adj_ii, None, None, None, True), "よくて")

        self.assertEqual(Te.conjugateTe(self.adj_ii_compound, None, None, None, False), "かっこよくて")
        self.assertEqual(Te.conjugateTe(self.adj_ii_compound, None, None, None, True), "かっこよくて")

        self.assertEqual(Te.conjugateTe(self.adj_na, None, None, None, False), "げんきで")
        self.assertEqual(Te.conjugateTe(self.adj_na, None, None, None, True), "元気で")


if __name__ == "__main__":
    unittest.main()
