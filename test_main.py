from unittest import TestCase

from main import SimilarityChecker


class TestSimilarityChecker(TestCase):
    def setUp(self):
        self.checker = SimilarityChecker()

    def test_same_length(self):
        ret = self.checker.check_length_similarity("ABC", "ABC")
        self.assertEqual(ret, 60)

    def test_over_than_twice_length(self):
        ret = self.checker.check_length_similarity("A", "ABC")
        self.assertEqual(ret, 0)
        ret = self.checker.check_length_similarity("ABC", "A")
        self.assertEqual(ret, 0)

    def test_different_length(self):
        ret = self.checker.check_length_similarity("ABCDE", "ABC")
        self.assertEqual(ret, 20)
        ret = self.checker.check_length_similarity("ABC", "ABCDE")
        self.assertEqual(ret, 20)
        ret = self.checker.check_length_similarity("ABCE", "ABC")
        self.assertEqual(ret, 40)
        ret = self.checker.check_length_similarity("ABCDEFDDG", "ABCASGD")
        self.assertEqual(ret, 42)
