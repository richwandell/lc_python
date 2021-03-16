from typing import List


class Solution:
    """
    Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number
    could represent. Return the answer in any order.

    A mapping of digit to letters (just like on the telephone buttons) is given below.
    Note that 1 does not map to any letters.
    """
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0: return []

        possible = [[], [], ["a", "b", "c"], ["d", "e", "f"], ["g", "h", "i"],
                            ["j", "k", "l"], ["m", "n", "o"], ["p", "q", "r", "s"],
                            ["t", "u", "v"], ["w", "x", "y", "z"]]

        def combine(current, letters):

            if len(letters) == 0: return current

            combs = []
            for letter in current:
                sub_combs = combine(letters[0], letters[1:])
                for sub_comb in sub_combs:
                    combs.append(letter + sub_comb)

            return combs

        letters = []
        for num in digits:
            letters.append(possible[int(num)])

        return combine(letters[0], letters[1:])


s = Solution()
print(s.letterCombinations("23"))
print(s.letterCombinations("2"))
print(s.letterCombinations(""))
