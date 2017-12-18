instructions = []

with open("in.txt", "r") as in_file:
	for line in in_file:
		instructions.append(line.split())

index = 0

last_sound_played = None
registers = {}


def get_value(register):
	value = 0
	try:
		value = int(register)
	except:
		registers.setdefault(register, 0)
		value = registers[register]
	return value


while index < len(instructions):
	instruction = instructions[index]
	if instruction[0] == "snd":
		last_sound_played = get_value(instruction[1])
	elif instruction[0] == "set":
		registers[instruction[1]] = get_value(instruction[2])
	elif instruction[0] == "add":
		registers.setdefault(instruction[1], 0)
		registers[instruction[1]] += get_value(instruction[2])
	elif instruction[0] == "mul":
		registers.setdefault(instruction[1], 0)
		registers[instruction[1]] *= get_value(instruction[2])
	elif instruction[0] == "mod":
		registers.setdefault(instruction[1], 0)
		registers[instruction[1]] %= get_value(instruction[2])
	elif instruction[0] == "rcv":
		if get_value(instruction[1]):
			break
	elif instruction[0] == "jgz":
		check = get_value(instruction[1])
		if check > 0:
			index += get_value(instruction[2])
			continue
	index += 1

print last_sound_played