severity = 0

with open("in.txt", "r") as in_file:
	for line in in_file:
		depth, drange = map(int, line.split(": "))
		if depth % (2*drange - 2) == 0:
			severity += depth * drange
print severity