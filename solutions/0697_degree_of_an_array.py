class Solution(object):
    def findShortestSubArray(self, nums):
        # Use a dictionary to record the frequency of each number.
        degree_dict = {}
        for num in nums:
            if num in degree_dict:
                degree_dict[num] += 1
            else:
                degree_dict[num] = 1

        # Find the number(s) with the highest frequency.
        degree = max(degree_dict.values())
        max_group = [key for key, value in degree_dict.items() if value == degree]
        min_length = []

        # Calculate the shortest subarray length for each candidate.
        for n in max_group:
            first_index = None
            last_index = None
            for index, num in enumerate(nums):
                if num == n:
                    if first_index is None:
                        first_index = index
                        last_index = index
                    else:
                        last_index = index
            min_length.append(last_index - first_index + 1)

        return min(min_length)

        
        