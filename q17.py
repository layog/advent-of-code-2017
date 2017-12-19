steps = 359

lock = [0]

next_num = 1
current_pos = 0

while next_num < 2018:
	next_pos = (current_pos + steps)%len(lock) + 1
	lock = lock[:next_pos] + [next_num] + lock[next_pos:]
	current_pos = next_pos
	next_num += 1

print lock[(current_pos+1)%len(lock)]
