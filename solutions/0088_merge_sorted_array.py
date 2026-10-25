class Solution(object):
    def merge(self, nums1, m, nums2, n):
        last_n1 = m - 1
        last_n2 = n - 1
        last_position = m + n - 1

        while last_n2 >= 0:
            # When m = 0, last_n1 = -1, In Python, nums1[-1] is 0
            if last_n1 < 0 or nums1[last_n1] < nums2[last_n2]:
                nums1[last_position] = nums2[last_n2]
                last_n2 -= 1
                last_position -= 1
            else:
                nums1[last_position] = nums1[last_n1]
                last_n1 -= 1
                last_position -= 1