from unittest import TestCase

from main import SimilarityChecker


class TestSimilarityChecker(TestCase):
    def setUp(self):
        self.checker = SimilarityChecker()

    def test_same_length(self):
        ret = self.checker.check_length_similarity("ABC", "ABC")
        self.assertEqual(ret, 60)
