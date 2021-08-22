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

        return_vals = []

        for i in range(n, -1, -1):
            opens, closes = [], []
            tmp = ""
            while len(closes) < n:
                if len(opens) == len(closes):
                    opens.append("(")
                    tmp += "("
                elif len(opens) == i:
                    closes.append(")")
                    tmp += ")"
                else:
                    opens.append("(")
                    tmp += "("
            return_vals.append(tmp)
        return return_vals


s = Solution()
print(s.generateParenthesis(3))