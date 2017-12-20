all_nodes = set()
all_children = set()

graph = {}
weights = {}

with open('in.txt', 'r') as in_file:
    for line in in_file:
        line = line.strip()
        if ' -> ' in line:
            node, children = line.split(' -> ')
        else:
            node, children = line, ''
        node, weight = node.split(' ', 1)
        weight = int(weight[1:-1])
        children = children.strip().split(", ")
        all_nodes.add(node)
        all_children = all_children | set(children)

        weights[node] = weight
        graph[node] = children

head = [x for x in (all_nodes - all_children)][0]

def get_wrong_disc(current):
    total_weight = weights[current]
    children_weight = []
    for child in graph[current]:
        if not child:
            continue
        wrong, weight, parent = get_wrong_disc(child)
        if wrong:
            return wrong, weight, parent
        children_weight.append(weight)

    total_weight += sum(children_weight)
    if not children_weight:
        return [], total_weight, None
    if len(set(children_weight)) != 1:
        return children_weight, graph[current], current
    return [], total_weight, None

def is_tree_balanced(current):
    total_weight = weights[current]
    children_weight = []
    for child in graph[current]:
        if not child:
            continue
        ans, weight = is_tree_balanced(child)
        if ans:
            return ans, weight
        children_weight.append(weight)
    if not children_weight:
        return True, total_weight
    if len(set(children_weight)) != 1:
        return False, total_weight
    return True, total_weight

wrong_weights, wrong_nodes, parent_node = get_wrong_disc(head)

if len(wrong_weights) > 2:
    temp_weights = sorted(wrong_weights)
    wrong_weight = None
    if temp_weights[0] == temp_weights[1]:
        wrong_weight = temp_weights[-1]
        difference = temp_weights[-1] - temp_weights[0]
    else:
        wrong_weight = temp_weights[0]
        difference = temp_weights[0] - temp_weights[-1]
    wrong_node = wrong_nodes[wrong_weights.index(wrong_weight)]
    print weights[wrong_node] - difference

else:
    difference = wrong_weights[0] - wrong_weights[1]
    weights[wrong_nodes[0]] -= difference
    if is_tree_balanced(head):
        print weights[wrong_nodes[0]]
    else:
        print weights[wrong_nodes[1]] + difference