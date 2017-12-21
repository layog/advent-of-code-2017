# The string repeats itself after every 60 iterations

program_length = 16
programs = [chr(x) for x in range(ord('a'), ord('a') + program_length)]
saved = programs[:]

with open('in.txt', "r") as in_file:
    moves = in_file.read().strip().split(",")


for i in range((10**9)%60):
    for j, move in enumerate(moves):
        # if programs == saved:
        #     print "At index {}, {}".format(i, j)
        if move[0] == "s":
            amount = int(move[1:])
            programs = programs[-amount:] + programs[:-amount]
        elif move[0] == "x":
            index1, index2 = map(int, move[1:].split("/"))
            programs[index1], programs[index2] = programs[index2], programs[index1]
        elif move[0] == "p":
            program1, program2 = move[1:].split("/")
            index1, index2 = programs.index(program1), programs.index(program2)
            programs[index1], programs[index2] = programs[index2], programs[index1]
        else:
            print "Unknown move"


print "".join(programs)