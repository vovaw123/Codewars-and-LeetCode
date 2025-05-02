# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: Optional[TreeNode]
        :type key: int
        :rtype: Optional[TreeNode]
        """
        if root is None:
            return None

        if key == root.val:
            if root.right is None:
                return root.left
            if root.left is None:
                return root.right

            temp = root.right
            while not(temp.left is None):
                temp = temp.left
            root.val = temp.val
            root.right = self.deleteNode(root.right, temp.val)

        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        return root
