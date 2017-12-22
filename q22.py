
with open("in.txt", "r") as in_file:
	grid = []
	for line in in_file:
		grid.append(list(line.strip()))

height = len(grid)
width = len(grid[0])

x_diff, y_diff = int(width/2), int(height/2)

infected_locations = set()
for y_index, line in enumerate(grid):
	for x_index, node in enumerate(line):
		if node == "#":
			infected_locations.add((x_index - x_diff, y_diff - y_index))


next_look = {
	"l":{
		(1, 0): (0, 1),
		(0, 1): (-1, 0),
		(-1, 0): (0, -1),
		(0, -1): (1, 0)
	},
	"r":{
		(1, 0): (0, -1),
		(0, -1): (-1, 0),
		(-1, 0): (0, 1),
		(0, 1): (1, 0)
	}
}
current_loc = [0,0]
burst = 0
look = (0, 1)
infected_bursts = 0
while burst < 10000:
	if tuple(current_loc) in infected_locations:
		look = next_look['r'][look]
		infected_locations.remove(tuple(current_loc))
	else:
		look = next_look['l'][look]
		infected_locations.add(tuple(current_loc))
		infected_bursts += 1
	current_loc[0] += look[0]
	current_loc[1] += look[1]
	burst += 1

print infected_bursts
