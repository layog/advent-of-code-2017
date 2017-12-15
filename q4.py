valid_phrases = 0

with open("in.txt", "r") as in_file:
    for line in in_file:
        words = line.lower().strip().split()
        set_words = set(words)
        if len(set_words) == len(words):
            valid_phrases += 1
print valid_phrases
