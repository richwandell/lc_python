from typing import List


class Solution:

    def sortedSquares(self, A: List[int]) -> List[int]:
        i, j, k = 0, len(A) - 1, len(A) - 1

        n = [0] * len(A)
        while i < j:
            isq = A[i]**2
            jsq = A[j]**2

            if isq > jsq:
                n[k] = isq
                i += 1
            else:
                n[k] = jsq
                j -= 1
            k -= 1
        n[0] = A[i]**2
        return n


s = Solution()

# print(s.sortedSquares([-4,-1,0,3,10]))
print(s.sortedSquares([-7,-3,2,3,11]))


