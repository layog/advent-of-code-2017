pipes = {}

with open("in.txt", "r") as in_file:
    for line in in_file:
        parent, children = line.split("<->", 1)
        parent, children = int(parent), map(int, children.split(", "))
        pipes.setdefault(parent, set())
        for child in children:
        	pipes[parent].add(child)

seen = set()
to_check = [0]
while to_check:
	current = to_check.pop(0)
	seen.add(current)
	children = pipes[current]
	for child in children:
		if child not in seen:
			to_check.append(child)

print seen, len(seen)