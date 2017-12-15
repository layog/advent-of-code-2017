# HACK: I believe it is kinda brute force, a better solution might be
# available

import numpy as np

with open("in.txt", "r") as in_file:
    current_config = np.asarray(map(int, in_file.readline().strip().split()))

seen_config = set()
total_banks = len(current_config)

while tuple(current_config) not in seen_config:
    seen_config.add(tuple(current_config))
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

print len(seen_config)
