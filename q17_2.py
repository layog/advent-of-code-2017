steps = 359

lock = [0]

next_num = 1
current_pos = 0

num_pos = (current_pos + steps)%len(lock) + 1
num_after_0 = 1

current_pos = num_pos
next_num += 1

while next_num <= 50000000:
	next_pos = (current_pos + steps)%next_num + 1
	if next_pos == num_pos:
		num_after_0 = next_num
	current_pos = next_pos
	next_num += 1

print num_after_0
