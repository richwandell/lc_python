from typing import List


class Solution1:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        temp = []
        i, j = 0, 0


        while i < m and j < n:
            if nums1[i] < nums2[j]:
                temp.append(nums1[i])
                i += 1
            else:
                temp.append(nums2[j])
                j += 1

        if i < m:
            while i < m:
                temp.append(nums1[i])
                i += 1

        for k, e in enumerate(temp):
            nums1[k] = e

        if j < n:
            k = len(temp)
            while j < n:
                nums1[k] = nums2[j]
                j += 1
                k += 1



# s = Solution1()
# a = [1,2,3,0,0,0]
# b = [2,5,6]
# s.merge(a, 3, b, 3)
# print(a)
# a = [0]
# b = [1]
# s.merge(a, 0, b, 1)
# print(a)
# a = [2, 0]
# b = [1]
# s.merge(a, 1, b, 1)
# print(a)

class Solution2:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n == 0: return None
        i, j, k = len(nums1) - 1, m - 1, n - 1


        while True:

            if j == -1 or nums1[j] < nums2[k]:
                nums1[i] = nums2[k]
                k -= 1
            else:
                nums1[i] = nums1[j]
                j -= 1
            if k < 0:
                break
            i -= 1

s = Solution2()
a = [1,2,3,0,0,0]
b = [2,5,6]
s.merge(a, 3, b, 3)
print(a)
a = [0]
b = [1]
s.merge(a, 0, b, 1)
print(a)
a = [2, 0]
b = [1]
s.merge(a, 1, b, 1)
print(a)