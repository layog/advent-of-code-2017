from q10_2 import complete_hash

string_input = "xlqgujun"

grid = []

for x in range(128):
    this_string_input = list(string_input + "-" + str(x))
    this_string_input = [ord(letter) for letter in this_string_input]
    this_string_hash = complete_hash(this_string_input)

    this_string_hash = bin(int(this_string_hash, 16))[2:].zfill(128)
    this_string_hash = this_string_hash.replace('1', '#')
    this_string_hash = this_string_hash.replace('0', '.')

    grid.append(list(this_string_hash))

current_group = 0


def match_nearbys(location):
    if grid[location[0]][location[1]] != "#":
        return
    grid[location[0]][location[1]] = current_group
    if location[0] + 1 < 128:
        match_nearbys((location[0] + 1, location[1]))
    if location[0] - 1 >= 0:
        match_nearbys((location[0] - 1, location[1]))
    if location[1] + 1 < 128:
        match_nearbys((location[0], location[1] + 1))
    if location[1] - 1 >= 0:
        match_nearbys((location[0], location[1] - 1))

x_index = 0
while x_index < 128:
    y_index = 0
    while y_index < 128:
        if grid[x_index][y_index] == "#":
            current_group += 1
            match_nearbys((x_index, y_index))
        y_index += 1
    x_index += 1

print current_group
