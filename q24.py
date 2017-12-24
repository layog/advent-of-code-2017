with open('in.txt', 'r') as in_file:
    ports = []
    for line in in_file:
        ports.append(map(int, line.split('/')))

# Let's create a grid of the possible collections
# Manually adding the first node
possibilities = []

for index, port in enumerate(ports):
    if 0 in port:
        possibilities.append({"selected": set([index]),
            "next": sum(port),
            "strength": sum(port)})


finalized = []
while True:
    update = False
    new_options = []
    for possible_option in possibilities:
        this_option_updated = False
        for index, port in enumerate(ports):
            if index not in possible_option["selected"] and possible_option["next"] in port:
                new_possible_option = {
                    "next": possible_option["next"],
                    "selected": possible_option["selected"].copy(),
                    "strength": possible_option["strength"]
                }
                new_possible_option["next"] = sum(port) - new_possible_option["next"]
                new_possible_option["selected"].add(index)
                new_possible_option["strength"] += sum(port)
                new_options.append(new_possible_option)
                update = True
                this_option_updated = True
        if not this_option_updated:
            finalized.append(possible_option)

    if not update:
        break
    possibilities = new_options

max_strength = 0
for option in finalized:
    max_strength = max(max_strength, option["strength"])

print max_strength