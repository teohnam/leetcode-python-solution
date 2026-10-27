class Solution(object):
    def generate(self, numRows):
        result = []
        for row_num in range(1, numRows + 1):
            if row_num == 1:
                result.append([1])
            else:
                last_row = result[-1]
                this_row = [1]

                for i in range(len(last_row) - 1):
                    this_row.append(last_row[i] + last_row[i+1])

                this_row.append(1)
                result.append(this_row)
        
        return result

            