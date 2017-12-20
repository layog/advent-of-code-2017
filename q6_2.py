import numpy as np

with open("in.txt", "r") as in_file:
    current_config = np.asarray(map(int, in_file.readline().strip().split()))

seen_config = {}
total_banks = len(current_config)

index = 0
while tuple(current_config) not in seen_config:
    seen_config[tuple(current_config)] = index
    index += 1
    max_blocks = max(current_config)
    max_blocks_index = np.where(current_config==max_blocks)[0][0]

    current_config[max_blocks_index] = 0

    num_add_to_all = max_blocks/total_banks

    current_config += num_add_to_all

    end_index = (max_blocks_index + max_blocks - (num_add_to_all * total_banks))%total_banks

    if end_index == max_blocks_index:
        continue
    if end_index < max_blocks_index:
        current_config[:end_index+1] += 1
        current_config[max_blocks_index+1:] += 1
    else:
        current_config[max_blocks_index+1:end_index+1] += 1

print index - seen_config[tuple(current_config)]