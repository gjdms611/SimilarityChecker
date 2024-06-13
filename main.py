class SimilarityChecker:
    def __init__(self):
        pass

    def check_length_similarity(self, param, param1):
        length1 = len(param)
        length2 = len(param1)
        if length1 == length2:
            return 60
        elif length1 * 2 < length2 or length1 > length2 * 2:
            return 0
        return 0
