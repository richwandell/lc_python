class Solution:
    def isPalindrome(self, s: str) -> bool:
        j, k = 0, len(s) - 1

        while j <= k:
            if not s[j].isalpha():
                j += 1
                continue
            if not s[k].isalpha():
                k -= 1
                continue

            if s[j].lower() != s[k].lower():
                return False
            j += 1
            k -= 1
        return True


s = Solution()

# print(s.isPalindrome("A man, a plan, a canal: Panama"))
# print(s.isPalindrome("race a car"))
print(s.isPalindrome("0P"))
