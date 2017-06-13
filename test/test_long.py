import unittest
import conj.Word as Word
import conj.Long as Long

class TestLong(unittest.TestCase):
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

    def testVerbLongPresentAffirmative(self):
        self.assertEqual(Long.conjugateLong(self.verb_ru, None, "present", "affirmative", False), "たべます")
        self.assertEqual(Long.conjugateLong(self.verb_ru, None, "present", "affirmative", True), "食べます")

        self.assertEqual(Long.conjugateLong(self.verb_u, None, "present", "affirmative", False), "かいます")
        self.assertEqual(Long.conjugateLong(self.verb_u, None, "present", "affirmative", True), "買います")

        self.assertEqual(Long.conjugateLong(self.verb_su, None, "present", "affirmative", False), "はなします")
        self.assertEqual(Long.conjugateLong(self.verb_su, None, "present", "affirmative", True), "話します")

        self.assertEqual(Long.conjugateLong(self.verb_ku, None, "present", "affirmative", False), "ききます")
        self.assertEqual(Long.conjugateLong(self.verb_ku, None, "present", "affirmative", True), "聞きます")

        self.assertEqual(Long.conjugateLong(self.verb_gu, None, "present", "affirmative", False), "およぎます")
        self.assertEqual(Long.conjugateLong(self.verb_gu, None, "present", "affirmative", True), "泳ぎます")

        self.assertEqual(Long.conjugateLong(self.verb_bu, None, "present", "affirmative", False), "あそびます")
        self.assertEqual(Long.conjugateLong(self.verb_bu, None, "present", "affirmative", True), "遊びます")

        self.assertEqual(Long.conjugateLong(self.verb_mu, None, "present", "affirmative", False), "のみます")
        self.assertEqual(Long.conjugateLong(self.verb_mu, None, "present", "affirmative", True), "飲みます")

        self.assertEqual(Long.conjugateLong(self.verb_nu, None, "present", "affirmative", False), "しにます")
        self.assertEqual(Long.conjugateLong(self.verb_nu, None, "present", "affirmative", True), "死にます")

        self.assertEqual(Long.conjugateLong(self.verb_uru, None, "present", "affirmative", False), "かえります")
        self.assertEqual(Long.conjugateLong(self.verb_uru, None, "present", "affirmative", True), "帰ります")

        self.assertEqual(Long.conjugateLong(self.verb_tsu, None, "present", "affirmative", False), "もちます")
        self.assertEqual(Long.conjugateLong(self.verb_tsu, None, "present", "affirmative", True), "持ちます")

        self.assertEqual(Long.conjugateLong(self.verb_iku, None, "present", "affirmative", False), "いきます")
        self.assertEqual(Long.conjugateLong(self.verb_iku, None, "present", "affirmative", True), "行きます")

        self.assertEqual(Long.conjugateLong(self.verb_suru, None, "present", "affirmative", False), "します")
        self.assertEqual(Long.conjugateLong(self.verb_suru, None, "present", "affirmative", True), "します")

        self.assertEqual(Long.conjugateLong(self.verb_kuru, None, "present", "affirmative", False), "きます")
        self.assertEqual(Long.conjugateLong(self.verb_kuru, None, "present", "affirmative", True), "来ます")

        self.assertEqual(Long.conjugateLong(self.verb_suru_compound, None, "present", "affirmative", False), "べんきょうします")
        self.assertEqual(Long.conjugateLong(self.verb_suru_compound, None, "present", "affirmative", True), "勉強します")

        self.assertEqual(Long.conjugateLong(self.verb_kuru_compound, None, "present", "affirmative", False), "もってきます")
        self.assertEqual(Long.conjugateLong(self.verb_kuru_compound, None, "present", "affirmative", True), "持って来ます")

    def testAdjLongPresentAffirmative(self):
        self.assertEqual(Long.conjugateLong(self.adj_i, None, "present", "affirmative", False), "かわいいです")
        self.assertEqual(Long.conjugateLong(self.adj_i, None, "present", "affirmative", True), "かわいいです")

        self.assertEqual(Long.conjugateLong(self.adj_ii, None, "present", "affirmative", False), "いいです")
        self.assertEqual(Long.conjugateLong(self.adj_ii, None, "present", "affirmative", True), "いいです")

        self.assertEqual(Long.conjugateLong(self.adj_ii_compound, None, "present", "affirmative", False), "かっこいいです")
        self.assertEqual(Long.conjugateLong(self.adj_ii_compound, None, "present", "affirmative", True), "かっこいいです")

        self.assertEqual(Long.conjugateLong(self.adj_na, None, "present", "affirmative", False), "げんきです")
        self.assertEqual(Long.conjugateLong(self.adj_na, None, "present", "affirmative", True), "元気です")

    def testVerbLongPastAffirmative(self):
        self.assertEqual(Long.conjugateLong(self.verb_ru, None, "past", "affirmative", False), "たべました")
        self.assertEqual(Long.conjugateLong(self.verb_ru, None, "past", "affirmative", True), "食べました")

        self.assertEqual(Long.conjugateLong(self.verb_u, None, "past", "affirmative", False), "かいました")
        self.assertEqual(Long.conjugateLong(self.verb_u, None, "past", "affirmative", True), "買いました")

        self.assertEqual(Long.conjugateLong(self.verb_su, None, "past", "affirmative", False), "はなしました")
        self.assertEqual(Long.conjugateLong(self.verb_su, None, "past", "affirmative", True), "話しました")

        self.assertEqual(Long.conjugateLong(self.verb_ku, None, "past", "affirmative", False), "ききました")
        self.assertEqual(Long.conjugateLong(self.verb_ku, None, "past", "affirmative", True), "聞きました")

        self.assertEqual(Long.conjugateLong(self.verb_gu, None, "past", "affirmative", False), "およぎました")
        self.assertEqual(Long.conjugateLong(self.verb_gu, None, "past", "affirmative", True), "泳ぎました")

        self.assertEqual(Long.conjugateLong(self.verb_bu, None, "past", "affirmative", False), "あそびました")
        self.assertEqual(Long.conjugateLong(self.verb_bu, None, "past", "affirmative", True), "遊びました")

        self.assertEqual(Long.conjugateLong(self.verb_mu, None, "past", "affirmative", False), "のみました")
        self.assertEqual(Long.conjugateLong(self.verb_mu, None, "past", "affirmative", True), "飲みました")

        self.assertEqual(Long.conjugateLong(self.verb_nu, None, "past", "affirmative", False), "しにました")
        self.assertEqual(Long.conjugateLong(self.verb_nu, None, "past", "affirmative", True), "死にました")

        self.assertEqual(Long.conjugateLong(self.verb_uru, None, "past", "affirmative", False), "かえりました")
        self.assertEqual(Long.conjugateLong(self.verb_uru, None, "past", "affirmative", True), "帰りました")

        self.assertEqual(Long.conjugateLong(self.verb_tsu, None, "past", "affirmative", False), "もちました")
        self.assertEqual(Long.conjugateLong(self.verb_tsu, None, "past", "affirmative", True), "持ちました")

        self.assertEqual(Long.conjugateLong(self.verb_iku, None, "past", "affirmative", False), "いきました")
        self.assertEqual(Long.conjugateLong(self.verb_iku, None, "past", "affirmative", True), "行きました")

        self.assertEqual(Long.conjugateLong(self.verb_suru, None, "past", "affirmative", False), "しました")
        self.assertEqual(Long.conjugateLong(self.verb_suru, None, "past", "affirmative", True), "しました")

        self.assertEqual(Long.conjugateLong(self.verb_kuru, None, "past", "affirmative", False), "きました")
        self.assertEqual(Long.conjugateLong(self.verb_kuru, None, "past", "affirmative", True), "来ました")

        self.assertEqual(Long.conjugateLong(self.verb_suru_compound, None, "past", "affirmative", False), "べんきょうしました")
        self.assertEqual(Long.conjugateLong(self.verb_suru_compound, None, "past", "affirmative", True), "勉強しました")

        self.assertEqual(Long.conjugateLong(self.verb_kuru_compound, None, "past", "affirmative", False), "もってきました")
        self.assertEqual(Long.conjugateLong(self.verb_kuru_compound, None, "past", "affirmative", True), "持って来ました")

    def testAdjLongPastAffirmative(self):
        self.assertEqual(Long.conjugateLong(self.adj_i, None, "past", "affirmative", False), "かわいかったです")
        self.assertEqual(Long.conjugateLong(self.adj_i, None, "past", "affirmative", True), "かわいかったです")

        self.assertEqual(Long.conjugateLong(self.adj_ii, None, "past", "affirmative", False), "よかったです")
        self.assertEqual(Long.conjugateLong(self.adj_ii, None, "past", "affirmative", True), "よかったです")

        self.assertEqual(Long.conjugateLong(self.adj_ii_compound, None, "past", "affirmative", False), "かっこよかったです")
        self.assertEqual(Long.conjugateLong(self.adj_ii_compound, None, "past", "affirmative", True), "かっこよかったです")

        self.assertEqual(Long.conjugateLong(self.adj_na, None, "past", "affirmative", False), "げんきでした")
        self.assertEqual(Long.conjugateLong(self.adj_na, None, "past", "affirmative", True), "元気でした")

    def testVerbLongPresentNegative(self):
        self.assertEqual(Long.conjugateLong(self.verb_ru, None, "present", "negative", False), "たべません")
        self.assertEqual(Long.conjugateLong(self.verb_ru, None, "present", "negative", True), "食べません")

        self.assertEqual(Long.conjugateLong(self.verb_u, None, "present", "negative", False), "かいません")
        self.assertEqual(Long.conjugateLong(self.verb_u, None, "present", "negative", True), "買いません")

        self.assertEqual(Long.conjugateLong(self.verb_su, None, "present", "negative", False), "はなしません")
        self.assertEqual(Long.conjugateLong(self.verb_su, None, "present", "negative", True), "話しません")

        self.assertEqual(Long.conjugateLong(self.verb_ku, None, "present", "negative", False), "ききません")
        self.assertEqual(Long.conjugateLong(self.verb_ku, None, "present", "negative", True), "聞きません")

        self.assertEqual(Long.conjugateLong(self.verb_gu, None, "present", "negative", False), "およぎません")
        self.assertEqual(Long.conjugateLong(self.verb_gu, None, "present", "negative", True), "泳ぎません")

        self.assertEqual(Long.conjugateLong(self.verb_bu, None, "present", "negative", False), "あそびません")
        self.assertEqual(Long.conjugateLong(self.verb_bu, None, "present", "negative", True), "遊びません")

        self.assertEqual(Long.conjugateLong(self.verb_mu, None, "present", "negative", False), "のみません")
        self.assertEqual(Long.conjugateLong(self.verb_mu, None, "present", "negative", True), "飲みません")

        self.assertEqual(Long.conjugateLong(self.verb_nu, None, "present", "negative", False), "しにません")
        self.assertEqual(Long.conjugateLong(self.verb_nu, None, "present", "negative", True), "死にません")

        self.assertEqual(Long.conjugateLong(self.verb_uru, None, "present", "negative", False), "かえりません")
        self.assertEqual(Long.conjugateLong(self.verb_uru, None, "present", "negative", True), "帰りません")

        self.assertEqual(Long.conjugateLong(self.verb_tsu, None, "present", "negative", False), "もちません")
        self.assertEqual(Long.conjugateLong(self.verb_tsu, None, "present", "negative", True), "持ちません")

        self.assertEqual(Long.conjugateLong(self.verb_iku, None, "present", "negative", False), "いきません")
        self.assertEqual(Long.conjugateLong(self.verb_iku, None, "present", "negative", True), "行きません")

        self.assertEqual(Long.conjugateLong(self.verb_suru, None, "present", "negative", False), "しません")
        self.assertEqual(Long.conjugateLong(self.verb_suru, None, "present", "negative", True), "しません")

        self.assertEqual(Long.conjugateLong(self.verb_kuru, None, "present", "negative", False), "きません")
        self.assertEqual(Long.conjugateLong(self.verb_kuru, None, "present", "negative", True), "来ません")

        self.assertEqual(Long.conjugateLong(self.verb_suru_compound, None, "present", "negative", False), "べんきょうしません")
        self.assertEqual(Long.conjugateLong(self.verb_suru_compound, None, "present", "negative", True), "勉強しません")

        self.assertEqual(Long.conjugateLong(self.verb_kuru_compound, None, "present", "negative", False), "もってきません")
        self.assertEqual(Long.conjugateLong(self.verb_kuru_compound, None, "present", "negative", True), "持って来ません")

    def testAdjLongPresentNegative(self):
        self.assertEqual(Long.conjugateLong(self.adj_i, None, "present", "negative", False), "かわいくないです")
        self.assertEqual(Long.conjugateLong(self.adj_i, None, "present", "negative", True), "かわいくないです")

        self.assertEqual(Long.conjugateLong(self.adj_ii, None, "present", "negative", False), "よくないです")
        self.assertEqual(Long.conjugateLong(self.adj_ii, None, "present", "negative", True), "よくないです")

        self.assertEqual(Long.conjugateLong(self.adj_ii_compound, None, "present", "negative", False), "かっこよくないです")
        self.assertEqual(Long.conjugateLong(self.adj_ii_compound, None, "present", "negative", True), "かっこよくないです")

        self.assertEqual(Long.conjugateLong(self.adj_na, None, "present", "negative", False), "げんきじゃないです")
        self.assertEqual(Long.conjugateLong(self.adj_na, None, "present", "negative", True), "元気じゃないです")

    def testVerbLongPastNegative(self):
        self.assertEqual(Long.conjugateLong(self.verb_ru, None, "past", "negative", False), "たべませんでした")
        self.assertEqual(Long.conjugateLong(self.verb_ru, None, "past", "negative", True), "食べませんでした")

        self.assertEqual(Long.conjugateLong(self.verb_u, None, "past", "negative", False), "かいませんでした")
        self.assertEqual(Long.conjugateLong(self.verb_u, None, "past", "negative", True), "買いませんでした")

        self.assertEqual(Long.conjugateLong(self.verb_su, None, "past", "negative", False), "はなしませんでした")
        self.assertEqual(Long.conjugateLong(self.verb_su, None, "past", "negative", True), "話しませんでした")

        self.assertEqual(Long.conjugateLong(self.verb_ku, None, "past", "negative", False), "ききませんでした")
        self.assertEqual(Long.conjugateLong(self.verb_ku, None, "past", "negative", True), "聞きませんでした")

        self.assertEqual(Long.conjugateLong(self.verb_gu, None, "past", "negative", False), "およぎませんでした")
        self.assertEqual(Long.conjugateLong(self.verb_gu, None, "past", "negative", True), "泳ぎませんでした")

        self.assertEqual(Long.conjugateLong(self.verb_bu, None, "past", "negative", False), "あそびませんでした")
        self.assertEqual(Long.conjugateLong(self.verb_bu, None, "past", "negative", True), "遊びませんでした")

        self.assertEqual(Long.conjugateLong(self.verb_mu, None, "past", "negative", False), "のみませんでした")
        self.assertEqual(Long.conjugateLong(self.verb_mu, None, "past", "negative", True), "飲みませんでした")

        self.assertEqual(Long.conjugateLong(self.verb_nu, None, "past", "negative", False), "しにませんでした")
        self.assertEqual(Long.conjugateLong(self.verb_nu, None, "past", "negative", True), "死にませんでした")

        self.assertEqual(Long.conjugateLong(self.verb_uru, None, "past", "negative", False), "かえりませんでした")
        self.assertEqual(Long.conjugateLong(self.verb_uru, None, "past", "negative", True), "帰りませんでした")

        self.assertEqual(Long.conjugateLong(self.verb_tsu, None, "past", "negative", False), "もちませんでした")
        self.assertEqual(Long.conjugateLong(self.verb_tsu, None, "past", "negative", True), "持ちませんでした")

        self.assertEqual(Long.conjugateLong(self.verb_iku, None, "past", "negative", False), "いきませんでした")
        self.assertEqual(Long.conjugateLong(self.verb_iku, None, "past", "negative", True), "行きませんでした")

        self.assertEqual(Long.conjugateLong(self.verb_suru, None, "past", "negative", False), "しませんでした")
        self.assertEqual(Long.conjugateLong(self.verb_suru, None, "past", "negative", True), "しませんでした")

        self.assertEqual(Long.conjugateLong(self.verb_kuru, None, "past", "negative", False), "きませんでした")
        self.assertEqual(Long.conjugateLong(self.verb_kuru, None, "past", "negative", True), "来ませんでした")

        self.assertEqual(Long.conjugateLong(self.verb_suru_compound, None, "past", "negative", False), "べんきょうしませんでした")
        self.assertEqual(Long.conjugateLong(self.verb_suru_compound, None, "past", "negative", True), "勉強しませんでした")

        self.assertEqual(Long.conjugateLong(self.verb_kuru_compound, None, "past", "negative", False), "もってきませんでした")
        self.assertEqual(Long.conjugateLong(self.verb_kuru_compound, None, "past", "negative", True), "持って来ませんでした")

    def testAdjLongPastNegative(self):
        self.assertEqual(Long.conjugateLong(self.adj_i, None, "past", "negative", False), "かわいくなかったです")
        self.assertEqual(Long.conjugateLong(self.adj_i, None, "past", "negative", True), "かわいくなかったです")

        self.assertEqual(Long.conjugateLong(self.adj_ii, None, "past", "negative", False), "よくなかったです")
        self.assertEqual(Long.conjugateLong(self.adj_ii, None, "past", "negative", True), "よくなかったです")

        self.assertEqual(Long.conjugateLong(self.adj_ii_compound, None, "past", "negative", False), "かっこよくなかったです")
        self.assertEqual(Long.conjugateLong(self.adj_ii_compound, None, "past", "negative", True), "かっこよくなかったです")

        self.assertEqual(Long.conjugateLong(self.adj_na, None, "past", "negative", False), "げんきじゃないでした")
        self.assertEqual(Long.conjugateLong(self.adj_na, None, "past", "negative", True), "元気じゃないでした")


if __name__ == "__main__":
    unittest.main()
