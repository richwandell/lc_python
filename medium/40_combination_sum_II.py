from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        answers = []
        used_answers = {}
        visited = {}

        def backtrack(items=[], used_items=set(), total=0):

            def check_total():
                if total == target:
                    s = tuple(sorted(items[:]))
                    if s not in used_answers:
                        used_answers[s] = True
                        answers.append(items[:])
            check_total()
            visited[tuple(sorted(used_items))] = total

            if total < target:
                for i, num in enumerate(candidates):
                    if i not in used_items:
                        used_items.add(i)
                        items.append(num)
                        key = tuple(sorted(used_items))
                        if key in visited:
                            total = visited[key]
                            check_total()
                            if total != target:
                                total -= num
                        else:
                            backtrack(items, used_items, total+num)
                        items.pop()
                        used_items.remove(i)

        backtrack([], set(), 0)
        return answers

s = Solution()
# print(s.combinationSum2([10,1,2,7,6,1,5], 8))
print(s.combinationSum2([3,1,3,5,1,1], 8))