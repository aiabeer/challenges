def detect_anagrams(word, candidates):
    word = word.lower()
    sorted_word = sorted(word)
    anagrams = []
    for candidate in candidates:
        if candidate.lower() != word and sorted(candidate.lower()) == sorted_word:
            anagrams.append(candidate)
    return anagrams