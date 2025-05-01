# Pre-order traversal
def pre_order(node):
    if node is None:
        return []
    current = [node.data]
    left = pre_order(node.left)
    right = pre_order(node.right)
    return current + left + right

# In-order traversal
def in_order(node):
    if node is None:
        return []
    left = in_order(node.left)
    current = [node.data]
    right = in_order(node.right)

    return left + current + right

# Post-order traversal
def post_order(node):
    if node is None:
        return []

#     result = []
#     left = post_order(node.left)
#     right = post_order(node.right)
#     if left:
#         result.append(left)
#     if right:
#         result.append(right)
#     result.append(str(node.data))

#     line = ' '.join(result)
#     linelist = line.split()
#     return linelist
    left = post_order(node.left)
    right = post_order(node.right)
    current = [node.data]

    return left + right + current
  
