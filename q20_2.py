import numpy as np
import warnings

warnings.filterwarnings('error')


def get_possible_roots(a, b, c):
    epsilon = 10**-5
    try:
        root_value = pow(b**2 - 4*a*c, 0.5)
    except:
        # A warning is raised if the above is less than 0
        return []
    
    if root_value - int(root_value) > epsilon:
        return []

    if a != 0:
        t1 = (-1*b + int(root_value))/(2.0*a)
        t2 = (-1*b - int(root_value))/(2.0*a)
    elif b != 0:
        t1 = t2 = -(c)/float(b)
    else:
        if c == 0:
            return "all"
        else:
            return []

    times = []
    if t1 > 0 and t1 - int(t1) < epsilon:
        times.append(int(t1))

    if t2 > 0 and t2 - int(t2) < epsilon:
        times.append(int(t2))
    
    return list(set(times))



def get_collision_time(particle1, particle2):
    acc1 = np.array(particle1["acceleration"])
    acc2 = np.array(particle2["acceleration"])
    vel1 = np.array(particle1["velocity"])
    vel2 = np.array(particle2["velocity"])
    pos1 = np.array(particle1["position"])
    pos2 = np.array(particle2["position"]) 

    a = acc1 - acc2
    b = (2*vel1 + acc1) - (2*vel2 + acc2)
    c = 2*(pos1 - pos2)

    times_x = get_possible_roots(a[0], b[0], c[0])
    times_y = get_possible_roots(a[1], b[1], c[1])
    times_z = get_possible_roots(a[2], b[2], c[2])

    collision_times = None

    if times_x != "all":
        collision_times = set(times_x)
    if times_y != "all":
        if collision_times is not None:
            collision_times = collision_times.intersection(set(times_y))
        else:
            collision_times = set(times_y)
    if times_z != "all":
        if collision_times is not None:
            collision_times = collision_times.intersection(set(times_z))
        else:
            collision_times = set(times_z)

    if not collision_times:
        return None

    collision_times = list(collision_times)
    collision_times.sort()
    return collision_times[0]


particles = []
with open("in.txt", "r") as in_file:
    for index, line in enumerate(in_file):
        position, velocity, acceleration = line.split(", ")
        position = position.strip()
        velocity = velocity.strip()
        acceleration = acceleration.strip()
        particle = {}
        particle["position"] = map(int, position[3:-1].split(","))
        particle["velocity"] = map(int, velocity[3:-1].split(","))
        particle["acceleration"] = map(int, acceleration[3:-1].split(","))
        particle["index"] = index
        particles.append(particle.copy())

collisions = []

for index1 in range(len(particles) - 1):
    for index2 in range(index1+1, len(particles)):
        collision_time = get_collision_time(particles[index1], particles[index2])
        if collision_time:
            collisions.append([collision_time, particles[index1], particles[index2]])

collisions.sort(key=lambda x: x[0])


remaining = set()
for particle in particles:
    remaining.add(particle["index"])

while collisions:
    current_time = collisions[0][0]
    current_set = set()
    while collisions[0][0] == current_time:
        collision_time, particle1, particle2 = collisions.pop(0)
        p1_index, p2_index = particle1["index"], particle2["index"]
        particle1_remains = (p1_index in remaining) or (p1_index in current_set)
        particle2_remains = (p2_index in remaining) or (p2_index in current_set)

        if particle1_remains and particle2_remains:
            if p1_index in remaining:
                remaining.remove(p1_index)
            if p2_index in remaining:
                remaining.remove(p2_index)
            current_set.add(p1_index)
            current_set.add(p2_index)

        if not collisions:
            break

print len(remaining)