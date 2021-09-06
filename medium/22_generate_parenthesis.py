from typing import List


class Solution:
    """
    Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.



Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]
    """
    def generateParenthesis(self, n: int) -> List[str]:

        answer = []
        def gen(items = [], l=0, r=0):

            if len(items) == 2*n:
                answer.append("".join(items))
                return
            if l < n:
                items.append("(")
                gen(items, l+1, r)
                items.pop()

            if r < l:
                items.append(")")
                gen(items, l, r+1)
                items.pop()

        gen([], 0)
        return answer

s = Solution()
print(s.generateParenthesis(3))