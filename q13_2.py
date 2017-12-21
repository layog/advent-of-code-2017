# depth + delay should not be divisible by (2*drange - 2)
# So, delay should not be equal to (drange-1)*2*x + depth

all_scanners = []

with open("in.txt", "r") as in_file:
    for line in in_file:
        depth, drange = map(int, line.split(": "))
        all_scanners.append((depth, drange))

delay = 0
while True:
    done = True
    for depth, drange in all_scanners:
        if (depth + delay)%(2*drange - 2) == 0:
            done = False
            break
    if done:
        break
    delay += 1

print delay