from tree import Node, insert

def get_min_value_node(node):
    current = node
    while current.left is not None:
        current = current.left
    return current


if __name__ == '__main__':
    # Test
    root = Node(5)
    root = insert(root, 3)
    root = insert(root, 2)
    root = insert(root, 4)
    root = insert(root, 7)
    root = insert(root, 6)
    root = insert(root, 8)
    root = insert(root, 1)
    print(root)

    print(f"Min elem: {get_min_value_node(root).val}")