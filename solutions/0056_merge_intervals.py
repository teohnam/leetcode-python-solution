class Solution(object):
    def merge(self, intervals):
        intervals.sort()
        result = []
        for i in range(len(intervals)):
            if result:
                # Compare current item with the last item in the result list
                if result[-1][1] >= intervals[i][0]:
                    result[-1] = [result[-1][0],  max(result[-1][1], intervals[i][1])]
                else: 
                    result.append(intervals[i])
            else:       
                result.append(intervals[i])      

        return result
