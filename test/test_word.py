import unittest
import conj.Word as Word

class TestWord(unittest.TestCase):
    def setUp(self):
        pass

    def testGroup(self):
        self.assertRaises(ValueError, Word.Adjective, None, None, None, None)
        self.assertIsInstance(Word.Adjective(None, None, None, "い"), Word.Adjective)
        self.assertIsInstance(Word.Adjective(None, None, None, "いい"), Word.Adjective)
        self.assertIsInstance(Word.Adjective(None, None, None, "な"), Word.Adjective)

        self.assertRaises(ValueError, Word.Verb, None, None, None, None)
        self.assertIsInstance(Word.Verb(None, None, None, "う"), Word.Verb)
        self.assertIsInstance(Word.Verb(None, None, None, "る"), Word.Verb)
        self.assertIsInstance(Word.Verb(None, None, None, "irregular"), Word.Verb)

    def testKanji(self):
        verb = Word.Verb("かう", "買う", "To Buy", "う")
        adj = Word.Adjective("げんき", "元気", "Healthy/Energetic", "な")

        self.assertEqual(verb.word_to_conjugate(True), "買う")
        self.assertEqual(verb.word_to_conjugate(False), "かう")

        self.assertEqual(adj.word_to_conjugate(True), "元気")
        self.assertEqual(adj.word_to_conjugate(False), "げんき")

    def testStem(self):
        u_verb = Word.Verb("かう", "買う", "To Buy", "う")
        ru_verb = Word.Verb("たべる", "食べる", "To Eat", "る")
        suru_verb = Word.Verb("する", None, "To Listen", "irregular")
        kuru_verb = Word.Verb("くる", "来る", "To Listen", "irregular")

        na_adj = Word.Adjective("げんき", "元気", "Healthy/Energetic", "な")
        ii_adj = Word.Adjective("いい", None, "Good", "いい")
        i_adj = Word.Adjective("たかい", "高い", "Cute", "い")

        self.assertEqual(u_verb.stem(True), "買い")
        self.assertEqual(u_verb.stem(False), "かい")
        self.assertEqual(ru_verb.stem(True), "食べ")
        self.assertEqual(ru_verb.stem(False), "たべ")
        self.assertEqual(suru_verb.stem(True), "し")
        self.assertEqual(suru_verb.stem(False), "し")
        self.assertEqual(kuru_verb.stem(True), "来")
        self.assertEqual(kuru_verb.stem(False), "き")

        self.assertEqual(na_adj.stem(True), "元気")
        self.assertEqual(na_adj.stem(False), "げんき")
        self.assertEqual(ii_adj.stem(True), "よ")
        self.assertEqual(ii_adj.stem(False), "よ")
        self.assertEqual(i_adj.stem(True), "高")
        self.assertEqual(i_adj.stem(False), "たか")



if __name__ == "__main__":
    unittest.main()
