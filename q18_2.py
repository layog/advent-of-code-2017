instructions = []

with open("in.txt", "r") as in_file:
	for line in in_file:
		instructions.append(line.split())

index = {
	0: 0,
	1: 0
}
registers = {
	0: {'p': 0, 'pipeline': []},
	1: {'p': 1, 'pipeline': []}
}

execute = 0
not_moved = 0
program_1_send = 0

def get_value(program, register):
	value = 0
	try:
		value = int(register)
	except:
		registers[program].setdefault(register, 0)
		value = registers[program][register]
	return value

while index[0] < len(instructions) or index[1] < len(instructions):
	if not_moved > 4:
		break
	if index[execute] >= len(instructions):
		execute = 1 - execute
		continue
	instruction = instructions[index[execute]]
	if instruction[0] == "snd":
		if execute == 1:
			program_1_send += 1
		registers[1 - execute]["pipeline"].append(get_value(execute, instruction[1]))
	elif instruction[0] == "set":
		registers[execute][instruction[1]] = get_value(execute, instruction[2])
	elif instruction[0] == "add":
		registers[execute].setdefault(instruction[1], 0)
		registers[execute][instruction[1]] += get_value(execute, instruction[2])
	elif instruction[0] == "mul":
		registers[execute].setdefault(instruction[1], 0)
		registers[execute][instruction[1]] *= get_value(execute, instruction[2])
	elif instruction[0] == "mod":
		registers[execute].setdefault(instruction[1], 0)
		registers[execute][instruction[1]] %= get_value(execute, instruction[2])
	elif instruction[0] == "rcv":
		if not registers[execute]["pipeline"]:
			execute = 1 - execute
			not_moved += 1
			continue
		else:
			registers[execute][instruction[1]] = registers[execute]["pipeline"].pop(0)
	elif instruction[0] == "jgz":
		check = get_value(execute, instruction[1])
		if check > 0:
			index[execute] += get_value(execute, instruction[2])
			not_moved = 0
			continue
	index[execute] += 1
	not_moved = 0

print program_1_send