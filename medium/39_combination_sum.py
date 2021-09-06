from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        answers = []
        set_answers = {}

        def backtrack(items=[], total=0):
            if total == target:
                s = tuple(sorted(items))
                if s not in set_answers:
                    answers.append(items[:])
                    set_answers[s] = True
                return

            if total < target:
                for i, cand in enumerate(candidates):
                    items.append(cand)
                    backtrack(items, total+cand)
                    items.pop()

        backtrack([], 0)
        return answers


s = Solution()
print(s.combinationSum([2,3,6,7], 7))