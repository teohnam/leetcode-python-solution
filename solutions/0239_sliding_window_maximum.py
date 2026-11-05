class Solution(object):
    def maxSlidingWindow(self, nums, k):
        result = []
        # Use a monotonic decreasing deque to store indices whose corresponding values are in decreasing order.
        deque = []
        left_pointer = 0

        for i in range(len(nums)):
            # Remove the first index if it is outside the current window.
            if deque and deque[0] < left_pointer:
                deque.pop(0)

            # Remove indices from the back while their corresponding values are smaller than or equal to the current value.
            while deque and nums[deque[-1]] <= nums[i]:
                deque.pop()

            # Push the current index to deque
            deque.append(i)

            # Once the window reaches size k, the first index in the deque represents the maximum value in the current window.
            if i - left_pointer == k - 1:
                result.append(nums[deque[0]])
                left_pointer += 1
                
        return result