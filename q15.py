genA = 883
genB = 879

factorA = 16807
factorB = 48271

divide_by = 2147483647

gen_no = 0

num = 1<<16

found = 0
while gen_no < 4*(10**7):
	genA = (genA*factorA)%divide_by
	genB = (genB*factorB)%divide_by

	if genA%num == genB%num:
		found +=1

	gen_no += 1

print found

