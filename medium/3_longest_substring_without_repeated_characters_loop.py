class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chset = set([])
        i = 0
        start = 0
        current = 0
        while i < len(s):
            c = s[i]
            if c in chset:
                chset = set([])
                i = start
                start += 1
            else:
                chset.add(c)
            if len(chset) > current:
                current = len(chset)
            i += 1
        return current

s = Solution()

print(s.lengthOfLongestSubstring("qrsvbspk"))
print(s.lengthOfLongestSubstring("au"))
print(s.lengthOfLongestSubstring(" "))
print(s.lengthOfLongestSubstring("abcabcbb"))
print(s.lengthOfLongestSubstring("bbbbb"))
print(s.lengthOfLongestSubstring("pwwkew"))