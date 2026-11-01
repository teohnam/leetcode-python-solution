"""
DFS (Depth-First Search)
Explore every possible jump path to determine whether the last index is reachable.

Alternative: 
Use a list to store the result of each index, avoid repeated calculation.
memo = [None] * len(nums)
"""
class Solution(object):
    def canJump(self, nums):
        def recursive(index):
            # Reached the last index
            if index == len(nums) - 1:
                return True
            # Cannot move forward
            elif nums[index] == 0:
                return False

            # Try every possible jump from the current position
            for step in range(1, nums[index] + 1):
                if recursive(index + step):
                    return True
            
            return False

        return recursive(0)
        