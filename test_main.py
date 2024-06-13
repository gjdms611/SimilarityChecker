from unittest import TestCase

from main import SimilarityChecker


class TestSimilarityChecker(TestCase):
    def test_same_length(self):
        self.checker = SimilarityChecker()
        ret = self.checker.check_length_similarity("ABC", "ABC")
        self.assertEqual(ret, 60)
