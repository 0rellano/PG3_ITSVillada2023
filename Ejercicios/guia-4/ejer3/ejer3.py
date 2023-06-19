
def is_anagram(word1: str, word2: str) -> bool:
    list_word1 = list(word1.lower())
    list_word2 = list(word2.lower())

    list_word1.sort()
    list_word2.sort()

    return list_word1 == list_word2
