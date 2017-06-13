import unittest
import conj.Word as Word
import conj.Become as Become

class TestBecome(unittest.TestCase):
    def setUp(self):
        self.adj_i = Word.Adjective("かわいい", None, "Cute", "い")
        self.adj_ii = Word.Adjective("いい", None, "Good", "いい")
        self.adj_ii_compound = Word.Adjective("かっこいい", None, "Cool", "いい")
        self.adj_na = Word.Adjective("げんき", "元気", "Healthy/Energetic", "な")

    def testAdjBecomeShortPresentAffirmative(self):
        self.assertEqual(Become.conjugateBecome(self.adj_i, "short", "present", "affirmative", False), "かわいくなる")
        self.assertEqual(Become.conjugateBecome(self.adj_i, "short", "present", "affirmative", True), "かわいくなる")

        self.assertEqual(Become.conjugateBecome(self.adj_ii, "short", "present", "affirmative", False), "よくなる")
        self.assertEqual(Become.conjugateBecome(self.adj_ii, "short", "present", "affirmative", True), "よくなる")

        self.assertEqual(Become.conjugateBecome(self.adj_ii_compound, "short", "present", "affirmative", False), "かっこよくなる")
        self.assertEqual(Become.conjugateBecome(self.adj_ii_compound, "short", "present", "affirmative", True), "かっこよくなる")

        self.assertEqual(Become.conjugateBecome(self.adj_na, "short", "present", "affirmative", False), "げんきになる")
        self.assertEqual(Become.conjugateBecome(self.adj_na, "short", "present", "affirmative", True), "元気になる")

    def testAdjBecomePastAffirmative(self):
        self.assertEqual(Become.conjugateBecome(self.adj_i, "short", "past", "affirmative", False), "かわいくなった")
        self.assertEqual(Become.conjugateBecome(self.adj_i, "short", "past", "affirmative", True), "かわいくなった")

        self.assertEqual(Become.conjugateBecome(self.adj_ii, "short", "past", "affirmative", False), "よくなった")
        self.assertEqual(Become.conjugateBecome(self.adj_ii, "short", "past", "affirmative", True), "よくなった")

        self.assertEqual(Become.conjugateBecome(self.adj_ii_compound, "short", "past", "affirmative", False), "かっこよくなった")
        self.assertEqual(Become.conjugateBecome(self.adj_ii_compound, "short", "past", "affirmative", True), "かっこよくなった")

        self.assertEqual(Become.conjugateBecome(self.adj_na, "short", "past", "affirmative", False), "げんきになった")
        self.assertEqual(Become.conjugateBecome(self.adj_na, "short", "past", "affirmative", True), "元気になった")

    def testAdjBecomePresentNegative(self):
        self.assertEqual(Become.conjugateBecome(self.adj_i, "short", "present", "negative", False), "かわいくならない")
        self.assertEqual(Become.conjugateBecome(self.adj_i, "short", "present", "negative", True), "かわいくならない")

        self.assertEqual(Become.conjugateBecome(self.adj_ii, "short", "present", "negative", False), "よくならない")
        self.assertEqual(Become.conjugateBecome(self.adj_ii, "short", "present", "negative", True), "よくならない")

        self.assertEqual(Become.conjugateBecome(self.adj_ii_compound, "short", "present", "negative", False), "かっこよくならない")
        self.assertEqual(Become.conjugateBecome(self.adj_ii_compound, "short", "present", "negative", True), "かっこよくならない")

        self.assertEqual(Become.conjugateBecome(self.adj_na, "short", "present", "negative", False), "げんきにならない")
        self.assertEqual(Become.conjugateBecome(self.adj_na, "short", "present", "negative", True), "元気にならない")

    def testAdjBecomePastNegative(self):
        self.assertEqual(Become.conjugateBecome(self.adj_i, "short", "past", "negative", False), "かわいくならなかった")
        self.assertEqual(Become.conjugateBecome(self.adj_i, "short", "past", "negative", True), "かわいくならなかった")

        self.assertEqual(Become.conjugateBecome(self.adj_ii, "short", "past", "negative", False), "よくならなかった")
        self.assertEqual(Become.conjugateBecome(self.adj_ii, "short", "past", "negative", True), "よくならなかった")

        self.assertEqual(Become.conjugateBecome(self.adj_ii_compound, "short", "past", "negative", False), "かっこよくならなかった")
        self.assertEqual(Become.conjugateBecome(self.adj_ii_compound, "short", "past", "negative", True), "かっこよくならなかった")

        self.assertEqual(Become.conjugateBecome(self.adj_na, "short", "past", "negative", False), "げんきにならなかった")
        self.assertEqual(Become.conjugateBecome(self.adj_na, "short", "past", "negative", True), "元気にならなかった")


if __name__ == "__main__":
    unittest.main()
