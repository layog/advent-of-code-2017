genA = 883
genB = 879

factorA = 16807
factorB = 48271

divide_by = 2147483647

num = 1<<16

found = 0

foundA = None
foundB = None

run = "A"

gen_no = 0

while gen_no < 5*(10**6):
	if run == "A":
		genA = (genA*factorA)%divide_by
		if genA % 4 == 0:
			foundA = genA
			run = "B"
	if run == "B":
		genB = (genB*factorB)%divide_by
		if genB % 8 == 0:
			foundB = genB
			run = "A"
	if foundA is not None and foundB is not None:
		gen_no += 1
		if foundA%num == foundB%num:
			found +=1
		foundA = foundB = None

print found

