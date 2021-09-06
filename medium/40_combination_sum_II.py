from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        answers = []
        used_answers = {}
        candidates.sort()

        def backtrack(items=[], total=0, next_start=0):

            if total == target:
                s = tuple(sorted(items[:]))
                if s not in used_answers:
                    used_answers[s] = True
                    answers.append(items[:])

            if total < target:
                for i in range(next_start, len(candidates)):
                    if i > next_start and candidates[i] == candidates[i-1]:
                        continue
                    items.append(candidates[i])
                    backtrack(items, total+candidates[i], i+1)
                    items.pop()

        backtrack([], 0, 0)
        return answers

s = Solution()
print(s.combinationSum2([10,1,2,7,6,1,5], 8))
print(s.combinationSum2([3,1,3,5,1,1], 8))
print(s.combinationSum2([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1], 27))
print(s.combinationSum2([1,2], 4))