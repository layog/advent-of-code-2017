def update(location):
	current = 0
	nearbys = generate_nearbys(location)
	for nearby in nearbys:
		current += (filled.get(nearby[0], {})).get(nearby[1], 0)
	filled.setdefault(location[0], {})
	filled[location[0]].setdefault(location[1], current)
	return current


def generate_nearbys(location):
	tl = [location[0] - 1, location[1] + 1]
	t = [location[0], location[1] + 1]
	tr = [location[0] + 1, location[1] + 1]
	r = [location[0] + 1, location[1]]
	br = [location[0] + 1, location[1] - 1]
	b = [location[0], location[1] - 1]
	bl = [location[0] - 1, location[1] - 1]
	l = [location[0] - 1, location[1]]
	return (tl, t, tr, r, br, b, bl, l)


past = 1

filled = {0: {0: 1}}

cur_loc = [0,0]
multiplier = 1
index = 0

min_limit = 265149

while filled[cur_loc[0]][cur_loc[1]] <= min_limit:
	done = False
	if multiplier % 2 == 1:
		for x in range(multiplier):
			cur_loc[0] += 1
			ans = update(cur_loc)
			if ans > min_limit:
				done = True
				break
		if done:
			break
		for x in range(multiplier):
			cur_loc[1] += 1
			ans = update(cur_loc)
			if ans > min_limit:
				done = True
				break
	else:
		for x in range(multiplier):
			cur_loc[0] -= 1
			ans = update(cur_loc)
			if ans > min_limit:
				done = True
				break
		if done:
			break
		for x in range(multiplier):
			cur_loc[1] -= 1
			ans = update(cur_loc)
			if ans > min_limit:
				done = True
				break
	multiplier += 1

print ans
