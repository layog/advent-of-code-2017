with open("in.txt", "r") as in_file:
    stream = in_file.readline().strip()

total_score = 0
started_groups = 0
current_garbage = False
next_skip = False

garbage_chars = 0

for character in stream:
    if next_skip:
        assert(current_garbage)
        next_skip = False
        continue
    if current_garbage:
        if character == ">":
            current_garbage = False
        elif character == "!":
            next_skip = True
        else:
            garbage_chars += 1
    else:
        if character == "<":
            current_garbage = True
        elif character == "{":
            started_groups += 1
        elif character == "}":
            total_score += started_groups
            started_groups -= 1

print garbage_chars
