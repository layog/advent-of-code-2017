all_nodes = set()
all_children = set()

with open('in.txt', 'r') as in_file:
    for line in in_file:
        line = line.strip()
        if '->' in line:
            node, children = line.split('->')
        else:
            node, children = line, ''
        node = node.split(' ', 1)[0]
        children = children.strip().split(", ")
        all_nodes.add(node)
        all_children = all_children | set(children)

print all_nodes - all_children
