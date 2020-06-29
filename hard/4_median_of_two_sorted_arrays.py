from typing import List
import random, math


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        final_list = []
        n1i, n2i = 0, 0
        max = (len(nums1) + len(nums2)) / 2
        while len(final_list) <= max:
            if len(nums1) == n1i:
                final_list.append(nums2[n2i])
                n2i += 1
                continue

            if len(nums2) == n2i:
                final_list.append(nums1[n1i])
                n1i += 1
                continue

            if nums1[n1i] > nums2[n2i]:
                final_list.append(nums2[n2i])
                n2i += 1
            elif nums1[n1i] < nums2[n2i]:
                final_list.append(nums1[n1i])
                n1i += 1
            else:
                final_list.append(nums1[n1i])
                n1i += 1
                if len(final_list) >= max:
                    continue
                final_list.append(nums2[n2i])
                n2i += 1

        if (len(nums1) + len(nums2)) % 2 == 0:
            num1 = final_list[-2]
            num2 = final_list[-1]
            mid = (num1 + num2) / 2
        else:
            mid = final_list[-1]
        return mid




td1 = list(range(2, 25))
td2 = sorted(list([random.randint(0, 22) for x in range(9)]))

nums1 = [1, 3]
nums2 = [2]

nums1 = []
nums2 = [1]

nums1 = []
nums2 = [2]

nums1 = [1,2]
nums2 = [1,2]

s = Solution()
print(s.findMedianSortedArrays(nums1, nums2))
print(s.findMedianSortedArrays(td1, td2))