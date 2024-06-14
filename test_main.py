from unittest import TestCase

from main import SimilarityChecker


class TestSimilarityChecker(TestCase):
    def setUp(self):
        self.checker = SimilarityChecker()

    def test_same_length(self):
        self.assert_matched_result("ABC", "ABC", 60)

    def test_over_than_twice_length(self):
        self.assert_matched_result("A", "ABC", 0)
        self.assert_matched_result("ABC", "A", 0)

    def test_different_length(self):
        self.assert_matched_result("ABCDE", "ABC", 20)
        self.assert_matched_result("ABC", "ABCDE", 20)
        self.assert_matched_result("ABCE", "ABC", 40)
        self.assert_matched_result("ABCDEFDDG", "ABCASGD", 42)

    def assert_matched_result(self, str1, str2, score):
        ret = self.checker.check_length_similarity(str1, str2)
        self.assertEqual(ret, score)

    def test_same_alphabet(self):
        self.assert_matched_alphabet_result(40, "ABC", "ABC")

    def assert_matched_alphabet_result(self, score, str1, str2):
        ret = self.checker.check_alphabet_similarity(str1, str2)
        self.assertEqual(ret, score)
