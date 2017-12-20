# Position of any particle at time t will be (can be easily derived)
# x(0) + v(0)*t + a*(t)*(t+1)/2
# Based on this, the first metric is the absolute value of a
# The second metric is the dot product of (v(0) + a/2) and a
# The third is the absolute value of v(0)
# If other metrics can be based on x

particles = []

def get_absolute_acceleration(input_acc):
    return input_acc[0]**2 + input_acc[1]**2 + input_acc[2]**2


def get_second_metric_value(input_acc, input_velocity):
    t_factor = [input_velocity[0] + input_acc[0]/2.0,
                input_velocity[1] + input_acc[1]/2.0,
                input_velocity[2] + input_acc[2]/2.0]
    return t_factor[0]*input_acc[0] + t_factor[1]*input_acc[1] + t_factor[2]*input_acc[2]


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

particles.sort(key=lambda x: get_absolute_acceleration(x["acceleration"]))

min_acc = get_absolute_acceleration(particles[0]["acceleration"])
remaining_particles = []
for particle in particles:
    if get_absolute_acceleration(particle["acceleration"]) != min_acc:
        break
    remaining_particles.append(particle)

print remaining_particles

if len(remaining_particles) > 1:
    remaining_particles.sort(key=lambda x: get_second_metric_value(x["acceleration"],
                                                                   x["velocity"]))
    still_remains = []
    min_second_metric = get_second_metric_value(remaining_particles[0]["acceleration"],
                                                remaining_particles[0]["velocity"])
    for particle in remaining_particles:
        if get_second_metric_value(particle["acceleration"], particle["velocity"]) != min_second_metric:
            break
        still_remains.append(particle)

    print still_remains