grid = []

with open("in.txt", "r") as in_file:
	for line in in_file:
		grid.append(list(line[:-1]))

current_pos = [0, grid[0].index("|")]

seen = []
current_movement = "d"

def get_next_pos(current_pos, movement):
	if movement == "d":
		return current_pos[0] + 1,  current_pos[1]
	if movement == "u":
		return current_pos[0] - 1, current_pos[1]
	if movement == "r":
		return current_pos[0], current_pos[1] + 1
	if movement == "l":
		return current_pos[0], current_pos[1] - 1


while (0 <= current_pos[0] < len(grid)) and (0 <= current_pos[1] < len(grid[0])):
	char_at_current_pos = grid[current_pos[0]][current_pos[1]]
	if char_at_current_pos == " ":
		break
	if current_movement in ["d", "u"]:
		if char_at_current_pos not in ["|", "-"]:
			if char_at_current_pos != "+":
				seen.append(char_at_current_pos)
			else:
				current_movement = "l"
				next_pos = get_next_pos(current_pos, "l")
				if grid[next_pos[0]][next_pos[1]] == " ":
					current_movement = "r"
	else:
		if char_at_current_pos not in ["|", "-"]:
			if char_at_current_pos != "+":
				seen.append(char_at_current_pos)
			else:
				current_movement = "u"
				next_pos = get_next_pos(current_pos, "u")
				if grid[next_pos[0]][next_pos[1]] == " ":
					current_movement = "d"
	current_pos = get_next_pos(current_pos, current_movement)

print "".join(seen)
