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

possible_moves = motion.keys()

def get_moves_required(child_movement):
    moves_made = []

    while np.linalg.norm(child_movement) > 0.1:
        chosen = 'n'
        max_dot_product = -1.0
        for possible_move in possible_moves:
            this_dot_product = np.sum(np.dot(motion[possible_move],
                                      child_movement))
            if this_dot_product > max_dot_product:
                max_dot_product = this_dot_product
                chosen = possible_move
        moves_made.append(chosen)
        child_movement -= motion[chosen]

    return moves_made

farthest_motion = 0
farthest_steps = 0

with open("in.txt", "r") as in_file:
    all_movements = in_file.readline().strip().split(",")


for index, move in enumerate(all_movements):
    if index%1000 == 0:
        print index
    net_child_movement += motion[move]
    this_child_movement = np.copy(net_child_movement)
    if np.linalg.norm(this_child_movement) > farthest_motion:
        this_farthest_steps = len(get_moves_required(this_child_movement))
        if this_farthest_steps > farthest_steps:
            farthest_steps = this_farthest_steps
            farthest_motion = np.linalg.norm(this_child_movement)

print farthest_steps
print len(get_moves_required(net_child_movement))
