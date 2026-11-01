"""
BFS (Breadth-First Search)

Alternative approach:
Use level_size to store the number of nodes at the current level.
Process exactly level_size nodes from the front of the queue.
Append their children to the back of the queue.
"""
class Solution(object):
    def levelOrder(self, root):
        result = []
        queue = []

        if root:
            queue.append(root)

        while queue:
            sub = []

            # Store the children of the current level
            sub_queue = []

            # Visit every node at the current level and append its value
            for node in queue:
                sub.append(node.val)
                if node.left:
                    sub_queue.append(node.left)
                if node.right:
                    sub_queue.append(node.right)

            result.append(sub)

            # Move to the next level
            queue = sub_queue
        
        return result