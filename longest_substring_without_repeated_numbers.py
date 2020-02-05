class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        i = 0
        chset = set([])
        bhset = set([])
        while i < len(s):
            c = s[i]
            if c in chset:
                if len(bhset) < len(chset):
                    bhset = chset

            else:
                chset.add(c)
            i += 1
        return bhset


s = Solution()

print(s.lengthOfLongestSubstring("abcabcbb"))