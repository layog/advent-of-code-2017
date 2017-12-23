registers = {}
for register in range(ord('a'), ord('h')+1):
    registers[chr(register)] = 0


def get_value(register):
    value = 0
    try:
        value = int(register)
    except:
        registers.setdefault(register, 0)
        value = registers[register]
    return value


instructions = []
with open("in.txt", "r") as in_file:
    for line in in_file:
        instructions.append(line.strip().split())


index = 0
count_mul = 0


while index < len(instructions):
    instruction = instructions[index]
    if instruction[0] == "set":
        registers[instruction[1]] = get_value(instruction[2])
    elif instruction[0] == "sub":
        registers[instruction[1]] -= get_value(instruction[2])
    elif instruction[0] == "mul":
        registers[instruction[1]] *= get_value(instruction[2])
        count_mul += 1
    elif instruction[0] == "jnz":
        check = get_value(instruction[1])
        if check != 0:
            index += get_value(instruction[2])
            continue
    index += 1

print count_mul