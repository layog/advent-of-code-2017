pipes = {}

with open("in.txt", "r") as in_file:
    for line in in_file:
        parent, children = line.split("<->", 1)
        parent, children = int(parent), map(int, children.split(", "))
        pipes.setdefault(parent, set())
        for child in children:
            pipes[parent].add(child)

total_set = 0
while pipes:
    seen = set()
    total_set += 1
    to_check = [pipes.keys()[0]]
    while to_check:
        current = to_check.pop(0)
        if current not in pipes:
            continue
        seen.add(current)
        children = pipes.pop(current)
        for child in children:
            if child not in seen:
                to_check.append(child)
    # print seen

print total_set