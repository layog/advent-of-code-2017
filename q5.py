with open("in.txt", "r") as in_file:
    jump_instructions = map(int, (in_file.read()).strip().split())

total_jumps = 0
current_index = 0

while 0 <= current_index < len(jump_instructions):
    total_jumps += 1
    past_index = current_index
    current_index += jump_instructions[past_index]
    jump_instructions[past_index] += 1

print total_jumps
