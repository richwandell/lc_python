class Solution:

    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n == 1: return s
        ps = [[False for x in range(n)] for x in range(n)]

        largest = ""
        i = 0
        while i < n:
            ps[i][i] = True
            largest = s[i]
            i += 1

        i = 0
        while i < n - 1:
            if s[i] == s[i + 1]:
                largest = s[i] + s[i + 1]
                ps[i][i + 1] = True
            i += 1

        k = 3
        while k <= n:
            i = 0
            while i < (n - k + 1):
                j = i + k - 1
                if ps[i + 1][j - 1] and s[i] == s[j]:
                    ps[i][j] = True
                    if k > len(largest):
                        largest = s[i:j + 1]
                i += 1
            k += 1
        return largest





input1 = "babad"
input2= "cbbd"
input3 = "aaababa"

s = Solution()
out1 = s.longestPalindrome(input1)
out2 = s.longestPalindrome(input2)
out3 = s.longestPalindrome(input3)

print(out1, out2, out3)