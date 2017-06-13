import unittest
import conj.Word as Word
import conj.Seems as Seems

class TestSeems(unittest.TestCase):
    def setUp(self):
        self.adj_i = Word.Adjective("かわいい", None, "Cute", "い")
        self.adj_ii = Word.Adjective("いい", None, "Good", "いい")
        self.adj_ii_compound = Word.Adjective("かっこいい", None, "Cool", "いい")
        self.adj_na = Word.Adjective("げんき", "元気", "Healthy/Energetic", "な")

    def testAdjSeemsShortPresentAffirmative(self):
        self.assertEqual(Seems.conjugateSeems(self.adj_i, "short", "present", "affirmative", False), "かわいそうです")
        self.assertEqual(Seems.conjugateSeems(self.adj_i, "short", "present", "affirmative", True), "かわいそうです")

        self.assertEqual(Seems.conjugateSeems(self.adj_ii, "short", "present", "affirmative", False), "よさそうです")
        self.assertEqual(Seems.conjugateSeems(self.adj_ii, "short", "present", "affirmative", True), "よさそうです")

        self.assertEqual(Seems.conjugateSeems(self.adj_ii_compound, "short", "present", "affirmative", False), "かっこよさそうです")
        self.assertEqual(Seems.conjugateSeems(self.adj_ii_compound, "short", "present", "affirmative", True), "かっこよさそうです")

        self.assertEqual(Seems.conjugateSeems(self.adj_na, "short", "present", "affirmative", False), "げんきそうです")
        self.assertEqual(Seems.conjugateSeems(self.adj_na, "short", "present", "affirmative", True), "元気そうです")

    def testAdjSeemsPastAffirmative(self):
        self.assertEqual(Seems.conjugateSeems(self.adj_i, "short", "past", "affirmative", False), "かわいそうでした")
        self.assertEqual(Seems.conjugateSeems(self.adj_i, "short", "past", "affirmative", True), "かわいそうでした")

        self.assertEqual(Seems.conjugateSeems(self.adj_ii, "short", "past", "affirmative", False), "よさそうでした")
        self.assertEqual(Seems.conjugateSeems(self.adj_ii, "short", "past", "affirmative", True), "よさそうでした")

        self.assertEqual(Seems.conjugateSeems(self.adj_ii_compound, "short", "past", "affirmative", False), "かっこよさそうでした")
        self.assertEqual(Seems.conjugateSeems(self.adj_ii_compound, "short", "past", "affirmative", True), "かっこよさそうでした")

        self.assertEqual(Seems.conjugateSeems(self.adj_na, "short", "past", "affirmative", False), "げんきそうでした")
        self.assertEqual(Seems.conjugateSeems(self.adj_na, "short", "past", "affirmative", True), "元気そうでした")

    def testAdjSeemsPresentNegative(self):
        self.assertEqual(Seems.conjugateSeems(self.adj_i, "short", "present", "negative", False), "かわいくなそうです")
        self.assertEqual(Seems.conjugateSeems(self.adj_i, "short", "present", "negative", True), "かわいくなそうです")

        self.assertEqual(Seems.conjugateSeems(self.adj_ii, "short", "present", "negative", False), "よさなそうです")
        self.assertEqual(Seems.conjugateSeems(self.adj_ii, "short", "present", "negative", True), "よさなそうです")

        self.assertEqual(Seems.conjugateSeems(self.adj_ii_compound, "short", "present", "negative", False), "かっこよさなそうです")
        self.assertEqual(Seems.conjugateSeems(self.adj_ii_compound, "short", "present", "negative", True), "かっこよさなそうです")

        self.assertEqual(Seems.conjugateSeems(self.adj_na, "short", "present", "negative", False), "げんきじゃなそうです")
        self.assertEqual(Seems.conjugateSeems(self.adj_na, "short", "present", "negative", True), "元気じゃなそうです")

    def testAdjSeemsPastNegative(self):
        self.assertEqual(Seems.conjugateSeems(self.adj_i, "short", "past", "negative", False), "かわいくなそうでした")
        self.assertEqual(Seems.conjugateSeems(self.adj_i, "short", "past", "negative", True), "かわいくなそうでした")

        self.assertEqual(Seems.conjugateSeems(self.adj_ii, "short", "past", "negative", False), "よさなそうでした")
        self.assertEqual(Seems.conjugateSeems(self.adj_ii, "short", "past", "negative", True), "よさなそうでした")

        self.assertEqual(Seems.conjugateSeems(self.adj_ii_compound, "short", "past", "negative", False), "かっこよさなそうでした")
        self.assertEqual(Seems.conjugateSeems(self.adj_ii_compound, "short", "past", "negative", True), "かっこよさなそうでした")

        self.assertEqual(Seems.conjugateSeems(self.adj_na, "short", "past", "negative", False), "げんきじゃなそうでした")
        self.assertEqual(Seems.conjugateSeems(self.adj_na, "short", "past", "negative", True), "元気じゃなそうでした")


if __name__ == "__main__":
    unittest.main()
