def is_binary_tree(puzzle_input):
    orbits = list(map(lambda x: x.split(')'), puzzle_input))
    d = (list(zip(*orbits)))

    from collections import Counter
    return (max(Counter(d[0]).values()) <= 2) and (max(Counter(d[1]).values()) == 1)


def convert_input_to_dict(puzzle_input):
    """
    >>> convert_input_to_dict(['A)B', 'B)C', 'A)D'])
    {'A': ['B', 'D'], 'B': ['C']}
    """
    from collections import defaultdict
    d = defaultdict(list)
    for line in puzzle_input:
        center, planet = line.split(')')
        d[center].append(planet)
    return dict(d)


def get_all_orbiting_objects(puzzle_input):
    """
    >>> sorted(list(get_all_orbiting_objects(['B)C', 'A)B', 'A)D'])))
    ['B', 'C', 'D']
    """
    return set(map(lambda x: x.split(')')[1], puzzle_input))


def generate_tree_from_dict(value, input_dict):
    leafs = input_dict.get(value)
    if not leafs:
        return Node(value)
    if len(leafs) > 0:
        left = generate_tree_from_dict(leafs[0], input_dict)
        if len(leafs) > 1:
            right = generate_tree_from_dict(leafs[1], input_dict)
            return Node(value, left, right)
        return Node(value, left)


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def print_node(self):
        """
        >>> Node('A').print_node()
        A
        >>> Node('A', 'A1').print_node()
        + - A1
        A
        >>> Node('A', 'A1', 'A2').print_node()
        + - A1
        A
        + - A2
        """
        if self.left:
            print(f"+ - {self.left.value if isinstance(self.left, Node) else self.left}")
        print(f"{self.value}")
        if self.right:
            print(f"+ - {self.right.value if isinstance(self.right, Node) else self.right}")


class BinaryTree:
    def __init__(self, input_data, start):
        """
        >>> BinaryTree(['B)C', 'A)B', 'A)D'], 'A').node.print_node()
        + - B
        A
        + - D
        """
        input_dict = convert_input_to_dict(input_data)
        self.node = generate_tree_from_dict(start, input_dict)


def find_distance_in_tree(start, leaf):
    """
    >>> start = BinaryTree(['B)C', 'A)B', 'A)D'], 'A').node
    >>> find_distance_in_tree(start, 'B')
    1
    >>> find_distance_in_tree(start, 'C')
    2
    >>> start = BinaryTree(['COM)B', 'B)C', 'C)D', 'D)E', 'E)F', 'B)G', 'G)H', 'D)I', 'E)J', 'J)K', 'K)L'], 'COM').node
    >>> find_distance_in_tree(start, 'D')
    3
    >>> find_distance_in_tree(start, 'L')
    7
    >>> find_distance_in_tree(start, 'COM')
    0
    >>> start = BinaryTree(['B)C', 'A)B', 'A)D'], 'D').node
    >>> find_distance_in_tree(start, 'Z')
    -1
    """
    if not start:
        return -1
    dist = -1
    if start.value == leaf:
        return dist + 1
    else:
        dist = find_distance_in_tree(start.left, leaf)
        if dist >= 0:
            return dist + 1
        else:
            dist = find_distance_in_tree(start.right, leaf)
            if dist >= 0:
                return dist + 1
    return -1


def total_number_of_orbits(puzzle_input):
    """
    >>> total_number_of_orbits(['B)C', 'COM)B', 'COM)D'])
    4
    >>> total_number_of_orbits(['COM)B', 'B)C', 'C)D', 'D)E', 'E)F', 'B)G', 'G)H', 'D)I', 'E)J', 'J)K', 'K)L'])
    42
    """
    tree = BinaryTree(puzzle_input, 'COM').node
    objects = get_all_orbiting_objects(puzzle_input)
    return sum(map(lambda x: find_distance_in_tree(tree, x), objects))


def shortest_path_via(puzzle_input, via):
    """
    >>> shortest_path_via(['COM)B', 'B)C', 'C)D', 'D)E', 'E)F', 'B)G', 'G)H', 'D)I', 'E)J', 'J)K', 'K)L', 'K)YOU', 'I)SAN'], 'D')
    4
    >>> shortest_path_via(['COM)B', 'B)C', 'C)D', 'D)E', 'E)F', 'B)G', 'G)H', 'D)I', 'E)J', 'J)K', 'K)L', 'K)YOU', 'I)SAN'], 'E')

    """
    start = BinaryTree(puzzle_input, via).node
    part1 = find_distance_in_tree(start, 'YOU')
    part2 = find_distance_in_tree(start, 'SAN')
    if part1 != -1 and part2 != -1:
        return part1 + part2 - 2


def shortest_path_to_santa(puzzle_input):
    """
    >>> shortest_path_to_santa(['COM)B', 'B)C', 'C)D', 'D)E', 'E)F', 'B)G', 'G)H', 'D)I', 'E)J', 'J)K', 'K)L', 'K)YOU', 'I)SAN'])
    4
    """
    objects = get_all_orbiting_objects(puzzle_input)
    objects.add('COM')
    return min(dist for dist in map(lambda x: shortest_path_via(puzzle_input, x), objects) if dist)


if __name__ == "__main__":
    with open("./data/day06.txt") as f:
        puzzle_input = f.read().split()

    assert is_binary_tree(puzzle_input)

    print('PART ONE')
    print(total_number_of_orbits(puzzle_input))

    print('PART TWO')
    print(shortest_path_to_santa(puzzle_input))
