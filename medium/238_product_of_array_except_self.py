from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        length = len(nums)
        l = [0]*length
        r = [0]*length
        answers = [0]*length

        l[0] = 1
        for i in range(1, length):
            l[i] = l[i-1] * nums[i-1]

        r[len(nums)-1] = 1
        for i in reversed(range(length - 1)):
            r[i] = r[i+1] * nums[i+1]

        for i in range(length):
            answers[i] = l[i] * r[i]
        return answers



s = Solution()
print(s.productExceptSelf([1,2,3,4]))