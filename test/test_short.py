import unittest
import conj.Word as Word
import conj.Short as Short

class TestShort(unittest.TestCase):
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

    def testVerbShortPresentAffirmative(self):
        self.assertEqual(Short.conjugateShort(self.verb_ru, None, "present", "affirmative", False), "たべる")
        self.assertEqual(Short.conjugateShort(self.verb_ru, None, "present", "affirmative", True), "食べる")

        self.assertEqual(Short.conjugateShort(self.verb_u, None, "present", "affirmative", False), "かう")
        self.assertEqual(Short.conjugateShort(self.verb_u, None, "present", "affirmative", True), "買う")

        self.assertEqual(Short.conjugateShort(self.verb_su, None, "present", "affirmative", False), "はなす")
        self.assertEqual(Short.conjugateShort(self.verb_su, None, "present", "affirmative", True), "話す")

        self.assertEqual(Short.conjugateShort(self.verb_ku, None, "present", "affirmative", False), "きく")
        self.assertEqual(Short.conjugateShort(self.verb_ku, None, "present", "affirmative", True), "聞く")

        self.assertEqual(Short.conjugateShort(self.verb_gu, None, "present", "affirmative", False), "およぐ")
        self.assertEqual(Short.conjugateShort(self.verb_gu, None, "present", "affirmative", True), "泳ぐ")

        self.assertEqual(Short.conjugateShort(self.verb_bu, None, "present", "affirmative", False), "あそぶ")
        self.assertEqual(Short.conjugateShort(self.verb_bu, None, "present", "affirmative", True), "遊ぶ")

        self.assertEqual(Short.conjugateShort(self.verb_mu, None, "present", "affirmative", False), "のむ")
        self.assertEqual(Short.conjugateShort(self.verb_mu, None, "present", "affirmative", True), "飲む")

        self.assertEqual(Short.conjugateShort(self.verb_nu, None, "present", "affirmative", False), "しぬ")
        self.assertEqual(Short.conjugateShort(self.verb_nu, None, "present", "affirmative", True), "死ぬ")

        self.assertEqual(Short.conjugateShort(self.verb_uru, None, "present", "affirmative", False), "かえる")
        self.assertEqual(Short.conjugateShort(self.verb_uru, None, "present", "affirmative", True), "帰る")

        self.assertEqual(Short.conjugateShort(self.verb_tsu, None, "present", "affirmative", False), "もつ")
        self.assertEqual(Short.conjugateShort(self.verb_tsu, None, "present", "affirmative", True), "持つ")

        self.assertEqual(Short.conjugateShort(self.verb_iku, None, "present", "affirmative", False), "いく")
        self.assertEqual(Short.conjugateShort(self.verb_iku, None, "present", "affirmative", True), "行く")

        self.assertEqual(Short.conjugateShort(self.verb_suru, None, "present", "affirmative", False), "する")
        self.assertEqual(Short.conjugateShort(self.verb_suru, None, "present", "affirmative", True), "する")

        self.assertEqual(Short.conjugateShort(self.verb_kuru, None, "present", "affirmative", False), "くる")
        self.assertEqual(Short.conjugateShort(self.verb_kuru, None, "present", "affirmative", True), "来る")

        self.assertEqual(Short.conjugateShort(self.verb_suru_compound, None, "present", "affirmative", False), "べんきょうする")
        self.assertEqual(Short.conjugateShort(self.verb_suru_compound, None, "present", "affirmative", True), "勉強する")

        self.assertEqual(Short.conjugateShort(self.verb_kuru_compound, None, "present", "affirmative", False), "もってくる")
        self.assertEqual(Short.conjugateShort(self.verb_kuru_compound, None, "present", "affirmative", True), "持って来る")

    def testAdjShortPresentAffirmative(self):
        self.assertEqual(Short.conjugateShort(self.adj_i, None, "present", "affirmative", False), "かわいい")
        self.assertEqual(Short.conjugateShort(self.adj_i, None, "present", "affirmative", True), "かわいい")

        self.assertEqual(Short.conjugateShort(self.adj_ii, None, "present", "affirmative", False), "いい")
        self.assertEqual(Short.conjugateShort(self.adj_ii, None, "present", "affirmative", True), "いい")

        self.assertEqual(Short.conjugateShort(self.adj_ii_compound, None, "present", "affirmative", False), "かっこいい")
        self.assertEqual(Short.conjugateShort(self.adj_ii_compound, None, "present", "affirmative", True), "かっこいい")

        self.assertEqual(Short.conjugateShort(self.adj_na, None, "present", "affirmative", False), "げんきだ")
        self.assertEqual(Short.conjugateShort(self.adj_na, None, "present", "affirmative", True), "元気だ")

    def testVerbShortPastAffirmative(self):
        self.assertEqual(Short.conjugateShort(self.verb_ru, None, "past", "affirmative", False), "たべた")
        self.assertEqual(Short.conjugateShort(self.verb_ru, None, "past", "affirmative", True), "食べた")

        self.assertEqual(Short.conjugateShort(self.verb_u, None, "past", "affirmative", False), "かった")
        self.assertEqual(Short.conjugateShort(self.verb_u, None, "past", "affirmative", True), "買った")

        self.assertEqual(Short.conjugateShort(self.verb_su, None, "past", "affirmative", False), "はなした")
        self.assertEqual(Short.conjugateShort(self.verb_su, None, "past", "affirmative", True), "話した")

        self.assertEqual(Short.conjugateShort(self.verb_ku, None, "past", "affirmative", False), "きいた")
        self.assertEqual(Short.conjugateShort(self.verb_ku, None, "past", "affirmative", True), "聞いた")

        self.assertEqual(Short.conjugateShort(self.verb_gu, None, "past", "affirmative", False), "およいだ")
        self.assertEqual(Short.conjugateShort(self.verb_gu, None, "past", "affirmative", True), "泳いだ")

        self.assertEqual(Short.conjugateShort(self.verb_bu, None, "past", "affirmative", False), "あそんだ")
        self.assertEqual(Short.conjugateShort(self.verb_bu, None, "past", "affirmative", True), "遊んだ")

        self.assertEqual(Short.conjugateShort(self.verb_mu, None, "past", "affirmative", False), "のんだ")
        self.assertEqual(Short.conjugateShort(self.verb_mu, None, "past", "affirmative", True), "飲んだ")

        self.assertEqual(Short.conjugateShort(self.verb_nu, None, "past", "affirmative", False), "しんだ")
        self.assertEqual(Short.conjugateShort(self.verb_nu, None, "past", "affirmative", True), "死んだ")

        self.assertEqual(Short.conjugateShort(self.verb_uru, None, "past", "affirmative", False), "かえった")
        self.assertEqual(Short.conjugateShort(self.verb_uru, None, "past", "affirmative", True), "帰った")

        self.assertEqual(Short.conjugateShort(self.verb_tsu, None, "past", "affirmative", False), "もった")
        self.assertEqual(Short.conjugateShort(self.verb_tsu, None, "past", "affirmative", True), "持った")

        self.assertEqual(Short.conjugateShort(self.verb_iku, None, "past", "affirmative", False), "いった")
        self.assertEqual(Short.conjugateShort(self.verb_iku, None, "past", "affirmative", True), "行った")

        self.assertEqual(Short.conjugateShort(self.verb_suru, None, "past", "affirmative", False), "した")
        self.assertEqual(Short.conjugateShort(self.verb_suru, None, "past", "affirmative", True), "した")

        self.assertEqual(Short.conjugateShort(self.verb_kuru, None, "past", "affirmative", False), "きた")
        self.assertEqual(Short.conjugateShort(self.verb_kuru, None, "past", "affirmative", True), "来た")

        self.assertEqual(Short.conjugateShort(self.verb_suru_compound, None, "past", "affirmative", False), "べんきょうした")
        self.assertEqual(Short.conjugateShort(self.verb_suru_compound, None, "past", "affirmative", True), "勉強した")

        self.assertEqual(Short.conjugateShort(self.verb_kuru_compound, None, "past", "affirmative", False), "もってきた")
        self.assertEqual(Short.conjugateShort(self.verb_kuru_compound, None, "past", "affirmative", True), "持って来た")

    def testAdjShortPastAffirmative(self):
        self.assertEqual(Short.conjugateShort(self.adj_i, None, "past", "affirmative", False), "かわいかった")
        self.assertEqual(Short.conjugateShort(self.adj_i, None, "past", "affirmative", True), "かわいかった")

        self.assertEqual(Short.conjugateShort(self.adj_ii, None, "past", "affirmative", False), "よかった")
        self.assertEqual(Short.conjugateShort(self.adj_ii, None, "past", "affirmative", True), "よかった")

        self.assertEqual(Short.conjugateShort(self.adj_ii_compound, None, "past", "affirmative", False), "かっこよかった")
        self.assertEqual(Short.conjugateShort(self.adj_ii_compound, None, "past", "affirmative", True), "かっこよかった")

        self.assertEqual(Short.conjugateShort(self.adj_na, None, "past", "affirmative", False), "げんきだった")
        self.assertEqual(Short.conjugateShort(self.adj_na, None, "past", "affirmative", True), "元気だった")

    def testVerbShortPresentNegative(self):
        self.assertEqual(Short.conjugateShort(self.verb_ru, None, "present", "negative", False), "たべない")
        self.assertEqual(Short.conjugateShort(self.verb_ru, None, "present", "negative", True), "食べない")

        self.assertEqual(Short.conjugateShort(self.verb_u, None, "present", "negative", False), "かわない")
        self.assertEqual(Short.conjugateShort(self.verb_u, None, "present", "negative", True), "買わない")

        self.assertEqual(Short.conjugateShort(self.verb_su, None, "present", "negative", False), "はなさない")
        self.assertEqual(Short.conjugateShort(self.verb_su, None, "present", "negative", True), "話さない")

        self.assertEqual(Short.conjugateShort(self.verb_ku, None, "present", "negative", False), "きかない")
        self.assertEqual(Short.conjugateShort(self.verb_ku, None, "present", "negative", True), "聞かない")

        self.assertEqual(Short.conjugateShort(self.verb_gu, None, "present", "negative", False), "およがない")
        self.assertEqual(Short.conjugateShort(self.verb_gu, None, "present", "negative", True), "泳がない")

        self.assertEqual(Short.conjugateShort(self.verb_bu, None, "present", "negative", False), "あそばない")
        self.assertEqual(Short.conjugateShort(self.verb_bu, None, "present", "negative", True), "遊ばない")

        self.assertEqual(Short.conjugateShort(self.verb_mu, None, "present", "negative", False), "のまない")
        self.assertEqual(Short.conjugateShort(self.verb_mu, None, "present", "negative", True), "飲まない")

        self.assertEqual(Short.conjugateShort(self.verb_nu, None, "present", "negative", False), "しなない")
        self.assertEqual(Short.conjugateShort(self.verb_nu, None, "present", "negative", True), "死なない")

        self.assertEqual(Short.conjugateShort(self.verb_uru, None, "present", "negative", False), "かえらない")
        self.assertEqual(Short.conjugateShort(self.verb_uru, None, "present", "negative", True), "帰らない")

        self.assertEqual(Short.conjugateShort(self.verb_tsu, None, "present", "negative", False), "もたない")
        self.assertEqual(Short.conjugateShort(self.verb_tsu, None, "present", "negative", True), "持たない")

        self.assertEqual(Short.conjugateShort(self.verb_iku, None, "present", "negative", False), "いかない")
        self.assertEqual(Short.conjugateShort(self.verb_iku, None, "present", "negative", True), "行かない")

        self.assertEqual(Short.conjugateShort(self.verb_suru, None, "present", "negative", False), "しない")
        self.assertEqual(Short.conjugateShort(self.verb_suru, None, "present", "negative", True), "しない")

        self.assertEqual(Short.conjugateShort(self.verb_kuru, None, "present", "negative", False), "こない")
        self.assertEqual(Short.conjugateShort(self.verb_kuru, None, "present", "negative", True), "来ない")

        self.assertEqual(Short.conjugateShort(self.verb_suru_compound, None, "present", "negative", False), "べんきょうしない")
        self.assertEqual(Short.conjugateShort(self.verb_suru_compound, None, "present", "negative", True), "勉強しない")

        self.assertEqual(Short.conjugateShort(self.verb_kuru_compound, None, "present", "negative", False), "もってこない")
        self.assertEqual(Short.conjugateShort(self.verb_kuru_compound, None, "present", "negative", True), "持って来ない")

    def testAdjShortPresentNegative(self):
        self.assertEqual(Short.conjugateShort(self.adj_i, None, "present", "negative", False), "かわいくない")
        self.assertEqual(Short.conjugateShort(self.adj_i, None, "present", "negative", True), "かわいくない")

        self.assertEqual(Short.conjugateShort(self.adj_ii, None, "present", "negative", False), "よくない")
        self.assertEqual(Short.conjugateShort(self.adj_ii, None, "present", "negative", True), "よくない")

        self.assertEqual(Short.conjugateShort(self.adj_ii_compound, None, "present", "negative", False), "かっこよくない")
        self.assertEqual(Short.conjugateShort(self.adj_ii_compound, None, "present", "negative", True), "かっこよくない")

        self.assertEqual(Short.conjugateShort(self.adj_na, None, "present", "negative", False), "げんきじゃない")
        self.assertEqual(Short.conjugateShort(self.adj_na, None, "present", "negative", True), "元気じゃない")

    def testVerbShortPastNegative(self):
        self.assertEqual(Short.conjugateShort(self.verb_ru, None, "past", "negative", False), "たべなかった")
        self.assertEqual(Short.conjugateShort(self.verb_ru, None, "past", "negative", True), "食べなかった")

        self.assertEqual(Short.conjugateShort(self.verb_u, None, "past", "negative", False), "かわなかった")
        self.assertEqual(Short.conjugateShort(self.verb_u, None, "past", "negative", True), "買わなかった")

        self.assertEqual(Short.conjugateShort(self.verb_su, None, "past", "negative", False), "はなさなかった")
        self.assertEqual(Short.conjugateShort(self.verb_su, None, "past", "negative", True), "話さなかった")

        self.assertEqual(Short.conjugateShort(self.verb_ku, None, "past", "negative", False), "きかなかった")
        self.assertEqual(Short.conjugateShort(self.verb_ku, None, "past", "negative", True), "聞かなかった")

        self.assertEqual(Short.conjugateShort(self.verb_gu, None, "past", "negative", False), "およがなかった")
        self.assertEqual(Short.conjugateShort(self.verb_gu, None, "past", "negative", True), "泳がなかった")

        self.assertEqual(Short.conjugateShort(self.verb_bu, None, "past", "negative", False), "あそばなかった")
        self.assertEqual(Short.conjugateShort(self.verb_bu, None, "past", "negative", True), "遊ばなかった")

        self.assertEqual(Short.conjugateShort(self.verb_mu, None, "past", "negative", False), "のまなかった")
        self.assertEqual(Short.conjugateShort(self.verb_mu, None, "past", "negative", True), "飲まなかった")

        self.assertEqual(Short.conjugateShort(self.verb_nu, None, "past", "negative", False), "しななかった")
        self.assertEqual(Short.conjugateShort(self.verb_nu, None, "past", "negative", True), "死ななかった")

        self.assertEqual(Short.conjugateShort(self.verb_uru, None, "past", "negative", False), "かえらなかった")
        self.assertEqual(Short.conjugateShort(self.verb_uru, None, "past", "negative", True), "帰らなかった")

        self.assertEqual(Short.conjugateShort(self.verb_tsu, None, "past", "negative", False), "もたなかった")
        self.assertEqual(Short.conjugateShort(self.verb_tsu, None, "past", "negative", True), "持たなかった")

        self.assertEqual(Short.conjugateShort(self.verb_iku, None, "past", "negative", False), "いかなかった")
        self.assertEqual(Short.conjugateShort(self.verb_iku, None, "past", "negative", True), "行かなかった")

        self.assertEqual(Short.conjugateShort(self.verb_suru, None, "past", "negative", False), "しなかった")
        self.assertEqual(Short.conjugateShort(self.verb_suru, None, "past", "negative", True), "しなかった")

        self.assertEqual(Short.conjugateShort(self.verb_kuru, None, "past", "negative", False), "こなかった")
        self.assertEqual(Short.conjugateShort(self.verb_kuru, None, "past", "negative", True), "来なかった")

        self.assertEqual(Short.conjugateShort(self.verb_suru_compound, None, "past", "negative", False), "べんきょうしなかった")
        self.assertEqual(Short.conjugateShort(self.verb_suru_compound, None, "past", "negative", True), "勉強しなかった")

        self.assertEqual(Short.conjugateShort(self.verb_kuru_compound, None, "past", "negative", False), "もってこなかった")
        self.assertEqual(Short.conjugateShort(self.verb_kuru_compound, None, "past", "negative", True), "持って来なかった")

    def testAdjShortPastNegative(self):
        self.assertEqual(Short.conjugateShort(self.adj_i, None, "past", "negative", False), "かわいくなかった")
        self.assertEqual(Short.conjugateShort(self.adj_i, None, "past", "negative", True), "かわいくなかった")

        self.assertEqual(Short.conjugateShort(self.adj_ii, None, "past", "negative", False), "よくなかった")
        self.assertEqual(Short.conjugateShort(self.adj_ii, None, "past", "negative", True), "よくなかった")

        self.assertEqual(Short.conjugateShort(self.adj_ii_compound, None, "past", "negative", False), "かっこよくなかった")
        self.assertEqual(Short.conjugateShort(self.adj_ii_compound, None, "past", "negative", True), "かっこよくなかった")

        self.assertEqual(Short.conjugateShort(self.adj_na, None, "past", "negative", False), "げんきじゃなかった")
        self.assertEqual(Short.conjugateShort(self.adj_na, None, "past", "negative", True), "元気じゃなかった")


if __name__ == "__main__":
    unittest.main()
