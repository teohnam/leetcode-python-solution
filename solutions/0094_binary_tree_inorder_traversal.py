"""
Recursive
Visit nodes in inorder: Left -> Root -> Right.
"""
class Solution(object):
    def inorderTraversal(self, root):
        result = []

        def recursive(node):
            if node is not None:
                recursive(node.left)
                result.append(node.val)
                recursive(node.right)
        
        recursive(root)
        return result

"""
Iterative
1. Keep pushing the current node onto the stack and move to its left child.
2. When the current node is None, pop a node from the stack and append its value to the result.
3. Move to the popped node's right child.
4. Repeat until both the current node and stack are empty.
"""
class Solution(object):
    def inorderTraversal(self, root):
        result = []
        stack = []
        node  = root

        while node or stack:
            if node:
                stack.append(node)
                node = node.left
            else: 
                node = stack.pop()
                result.append(node.val)
                node = node.right

        return result
                