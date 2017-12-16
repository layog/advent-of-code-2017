import math
import numpy as np

motion = {
    "n": np.array([0, 1], dtype='float32'),
    "s": np.array([0, -1], dtype='float32'),
    "nw": np.array([math.sqrt(3)/2.0, 1/2.0], dtype='float32'),
    "ne": np.array([-math.sqrt(3)/2.0, 1/2.0], dtype='float32'),
    "sw": np.array([math.sqrt(3)/2.0, -1/2.0], dtype='float32'),
    "se": np.array([-math.sqrt(3)/2.0, -1/2.0], dtype='float32')
}

net_child_movement = np.array([0, 0], dtype='float32')

with open("in.txt", "r") as in_file:
    all_movements = in_file.readline().strip().split(",")

for move in all_movements:
    net_child_movement += motion[move]

possible_moves = motion.keys()
moves_made = []

while np.linalg.norm(net_child_movement) > 0.1:
    chosen = 'n'
    max_dot_product = -1.0
    for possible_move in possible_moves:
        this_dot_product = np.sum(np.dot(motion[possible_move],
                                  net_child_movement))
        if this_dot_product > max_dot_product:
            max_dot_product = this_dot_product
            chosen = possible_move
    moves_made.append(chosen)
    net_child_movement -= motion[chosen]

print moves_made, len(moves_made)
