from tree import Node, insert

def get_sum(node):
    if node is None:
        return 0
    return get_sum(node.left) + get_sum(node.right) + node.val


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

    print(f"Sum of elements: {get_sum(root)}")