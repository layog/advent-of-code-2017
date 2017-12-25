# schema = {
# 	"state": {
# 		0: {
# 			"value_to_write":
# 			"move": 'l, 'r',
# 			"nextState": 
# 		}
# 	}
# }


machine = {}

with open("in.txt", "r") as in_file:
	begin_state = in_file.readline().strip().split("state ")[1][:-1]
	disagnostic_steps = in_file.readline().split('after ')[1]
	disagnostic_steps = int(disagnostic_steps.split()[0])

	# Blank line
	in_file.readline()

	while True:
		state = in_file.readline().strip()
		if state:
			state = state[-2]
			num1 = int(in_file.readline().strip()[-2])
			val1 = int(in_file.readline().strip()[-2])
			move1 = in_file.readline().strip().split()[-1][:-1]
			next_state1 = in_file.readline().strip()[-2]

			num2 = int(in_file.readline().strip()[-2])
			val2 = int(in_file.readline().strip()[-2])
			move2 = in_file.readline().strip().split()[-1][:-1]
			next_state2 = in_file.readline().strip()[-2]
			machine[state] = {
				num1: {
					"value_to_write": val1,
					"move": move1,
					"nextState": next_state1
				},
				num2: {
					"value_to_write": val2,
					"move": move2,
					"nextState": next_state2
				}
			}

			# Dummy line
			in_file.readline()
		else:
			break

print machine

ones = set()

def get_val(location):
	if location in ones:
		return 1
	return 0

def set_val(location, value):
	if value == 0 and location in ones:
		ones.remove(location)
	if value == 1:
		ones.add(location)

current_loc = 0
step = 0
current_state = begin_state
while step < disagnostic_steps:
	value = get_val(current_loc)
	try:
		values_for_this_state = machine[current_state][value]
	except KeyError:
		print step, state, value
		raise
	value_to_write = values_for_this_state["value_to_write"]
	move = values_for_this_state["move"]
	next_state = values_for_this_state["nextState"]

	set_val(current_loc, value_to_write)
	current_state = next_state
	if move == "left":
		current_loc -= 1
	elif move == "right":
		current_loc += 1
	else:
		raise KeyError("Check the move value: {}".format(move))
	step += 1

print len(ones)
