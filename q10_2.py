def perform_rotation(nums_list, input_lengths):
    round_no = 0
    skip_size = 0
    total_rotation = 0

    def rotate_list(inp, rotation):
        temp = inp[:]
        rotation = rotation % len(temp)
        return temp[rotation:] + temp[:rotation]

    while round_no < 64:
        for length in input_lengths:
            nums_list = (nums_list[: length])[::-1] + nums_list[length:]
            rotation = (length + skip_size) % len(nums_list)
            skip_size += 1
            total_rotation += rotation

            nums_list = rotate_list(nums_list, rotation)

        round_no += 1

    total_rotation = len(nums_list) - (total_rotation % len(nums_list))
    nums_list = rotate_list(nums_list, total_rotation)

    return nums_list


def create_dense_hash(sparse_hash):
    dense_hash = []
    dense_hash_index = 0
    while dense_hash_index < 16:
        num_index = 0
        this_dense_hash = 0
        while num_index < 16:
            this_dense_hash ^= sparse_hash[dense_hash_index*16 + num_index]
            num_index += 1
        dense_hash.append(this_dense_hash)
        dense_hash_index += 1

    return dense_hash


def convert_to_hex(dense_hash):
    hex_hash = []
    for num in dense_hash:
        hex_num = hex(num)
        if len(hex_num) == 4:
            hex_hash.append(hex_num[2:])
        else:
            hex_hash.append("0" + hex_num[-1])

    return "".join(hex_hash)

def complete_hash(input_lengths):
    list_length = 256
    nums_list = range(list_length)

    input_lengths += [17, 31, 73, 47, 23]

    sparse_hash = perform_rotation(nums_list, input_lengths)
    dense_hash = create_dense_hash(sparse_hash)
    hex_hash = convert_to_hex(dense_hash)

    return hex_hash


if __name__ == "__main__":
    with open("in.txt", "r") as in_file:
        input_lengths = list(in_file.readline().strip())

    input_lengths = [ord(length) for length in input_lengths]

    hashed = complete_hash(input_lengths)
    print hashed