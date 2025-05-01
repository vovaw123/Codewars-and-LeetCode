def tree_by_levels(node):
    if node is None:
        return []

    result = []
    queue = [node]

    while len(queue) != 0:
        current = queue.pop(0)
        result.append(current.value)
        if not(current.left is None):
            queue.append(current.left)
        if not(current.right is None):
            queue.append(current.right)
    return result
