valid_phrases = 0

with open("in.txt", "r") as in_file:
    for line in in_file:
        words = line.lower().strip().split()
        sorted_words = []
        for word in words:
            word = list(word)
            word.sort()
            sorted_words.append("".join(word))
        set_sorted_words = set(sorted_words)
        if len(set_sorted_words) == len(sorted_words):
            valid_phrases += 1
print valid_phrases
