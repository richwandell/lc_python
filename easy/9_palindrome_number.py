class Solution:

    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False

        n = x
        new_number = 0
        while True:
            if n == 0: break
            ni = n % 10
            n = n // 10
            new_number *= 10
            new_number += ni
        return new_number == x


s = Solution()
print(s.isPalindrome(121))
print(s.isPalindrome(-121))
print(s.isPalindrome(10))
