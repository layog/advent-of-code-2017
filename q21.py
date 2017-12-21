config = (".#.","..#","###")
config = [list(x) for x in config]

enhancements = {}
with open("in.txt", "r") as in_file:
	for line in in_file:
		from_config, to_config = line.strip().split(" => ")
		from_config = from_config.split("/")
		to_config = to_config.split("/")
		from_config = [tuple(x) for x in from_config]
		to_config = [list(x) for x in to_config]
		enhancements[tuple(from_config)] = to_config

def rotate(input_config, rotation=1):
	rotated_config = input_config
	for x in range(rotation):
		rotated_config = zip(*rotated_config[::-1])
	return tuple(rotated_config)

def flip_x(input_config):
	return tuple([x[::-1] for x in input_config])

def flip_y(input_config):
	return input_config[::-1]

def check_enhancements(input_config):
	tupled_config = tuple([tuple(x) for x in input_config])
	for i in range(4):
		if tupled_config in enhancements:
			return enhancements[tupled_config]
		x_tupled_config = flip_x(tupled_config)
		if x_tupled_config in enhancements:
			return enhancements[x_tupled_config]
		y_tupled_config = flip_y(tupled_config)
		if y_tupled_config in enhancements:
			return enhancements[y_tupled_config]
		tupled_config = rotate(tupled_config)

	raise ValueError, input_config

def get_enhancement(input_config):
	if len(input_config) == 2 or len(input_config) == 3:
		return check_enhancements(input_config)

	output_config = []
	if len(input_config)%2 == 0:
		mod = 2
	else:
		mod = 3

	for x_index in range(len(input_config)/mod):
			output_config.append([])
			for y_index in range(len(input_config[0])/mod):
				to_update = [x[y_index*mod:(y_index+1)*mod] for x in input_config[x_index*mod:(x_index+1)*mod]]
				updated = get_enhancement(to_update)
				output_config[-1].append(updated)

	final_config = []
	# for block in output_config:
	# 	print block
	for block_index in range(len(output_config)):
		this_block =[[] for x in range(mod+1)]
		for bloc in output_config[block_index]:
			for index in range(mod+1):
				this_block[index] += bloc[index]
		for row in this_block:
			final_config.append(row[:])

	return final_config

for iteration in range(18):
	config = get_enhancement(config)

print sum(c.count('#') for c in config)
