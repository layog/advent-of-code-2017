# Notice that instructions 9-23 just repeats themselves because of two loops
# One at index 19 and another at index 23
# So the answer of that loop can simply be generated noticing the patern in the loop

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


def is_factorizable(b):
    for i in range(2, int(pow(b, 0.5) + 2)):
        if b%i == 0:
            return True
    return False




index = 0
registers['a'] = 1

while index < len(instructions):
    instruction = instructions[index]

    # Pattern in the loop
    if index == 10:
        if is_factorizable(registers['b']):
            registers['f'] = 0
        index = 24
        continue
    
    if instruction[0] == "set":
        registers[instruction[1]] = get_value(instruction[2])
    elif instruction[0] == "sub":
        registers[instruction[1]] -= get_value(instruction[2])
    elif instruction[0] == "mul":
        registers[instruction[1]] *= get_value(instruction[2])
    elif instruction[0] == "jnz":
        check = get_value(instruction[1])
        if check != 0:
            index += get_value(instruction[2])
            continue
    index += 1

print registers['h']