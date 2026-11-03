class Solution(object):
    def countAndSay(self, n):
        result = "1"

        for _ in range(n - 1):
            temp = []
            count = 1

            for i in range(1, len(result)):
                if result[i] == result[i - 1]:
                    count += 1
                else:
                    temp.append(str(count))
                    temp.append(result[i - 1])
                    count = 1

            temp.append(str(count))
            temp.append(result[-1])

            result = "".join(temp)

        return result