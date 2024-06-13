class SimilarityChecker:
    def __init__(self):
        pass

    def check_length_similarity(self, str1, str2):
        length1 = len(str1)
        length2 = len(str2)
        if length2 > length1:
            length1, length2 = length2, length1

        if length1 == length2:
            return 60
        elif length1 * 2 < length2:
            return 0
        return 0
