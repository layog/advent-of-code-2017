list_length = 256

nums_list = range(list_length)

with open("in.txt", "r") as in_file:
    input_lengths = map(int, in_file.readline().strip().split(","))

skip_size = 0

total_rotation = 0


def rotate_list(inp, rotation):
    temp = inp[:]
    rotation = rotation % len(temp)
    return temp[rotation:] + temp[:rotation]


for length in input_lengths:
    nums_list = (nums_list[: length])[::-1] + nums_list[length:]
    rotation = (length + skip_size) % len(nums_list)
    skip_size += 1
    total_rotation += rotation

    nums_list = rotate_list(nums_list, rotation)

total_rotation = len(nums_list) - (total_rotation % len(nums_list))
nums_list = rotate_list(nums_list, total_rotation)

print nums_list
