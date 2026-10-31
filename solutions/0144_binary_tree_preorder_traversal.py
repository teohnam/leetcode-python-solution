"""
Recursive
Visit nodes in preorder: Root -> Left -> Right.
"""
class Solution(object):
    def preorderTraversal(self, root):
        result = []
        def recursive(node):
            if node is not None:
                result.append(node.val)
                recursive(node.left)
                recursive(node.right)

        recursive(root)
        return result

"""
Iterative
Use a stack to keep track of nodes to visit.
- Pop a node and append its value to the result.
- Push its right child first, then its left child.
  (LIFO ensures the left child is visited first.)
"""
class Solution(object):
    def preorderTraversal(self, root):
        if root is None:
            return []
            
        result = []
        stack = []
        stack.append(root)

        while stack:
            node = stack.pop()
            result.append(node.val)

            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
            
        return result