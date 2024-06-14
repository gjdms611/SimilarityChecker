class SimilarityChecker:
    def __init__(self):
        pass

    def check_length_similarity(self, str1, str2):
        long_len = len(str1)
        short_len = len(str2)

        if short_len > long_len:
            long_len, short_len = short_len, long_len

        if long_len > short_len * 2:
            return 0

        return int((1 - ((long_len - short_len) / short_len)) * 60)

    def check_alphabet_similarity(self, str1, str2):
        return 40
