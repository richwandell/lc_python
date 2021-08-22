from typing import List


class Solution:
    """
    You are given a string s and an array of strings words of the same length. Return all starting indices of substring(s) in s that is a concatenation of each word in words exactly once, in any order, and without any intervening characters.
    You can return the answer in any order.

Example 1:

Input: s = "barfoothefoobarman", words = ["foo","bar"]
Output: [0,9]
Explanation: Substrings starting at index 0 and 9 are "barfoo" and "foobar" respectively.
The output order does not matter, returning [9,0] is fine too.
Example 2:

Input: s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]
Output: []
Example 3:

Input: s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]
Output: [6,9,12]
    """
    def findSubstring(self, s: str, words: List[str]) -> List[int]:

        def matches(st, words):
            if len(st) == 0:
                return True
            for i, word in enumerate(words):
                if st[0:len(words[0])] == word:
                    st = st[len(words[0]):]
                    return matches(st, words[:i] + words[i+1:])
            return False


        word_length = len(words[0])*len(words)
        start = 0
        current = ""
        all_matches = []
        while start < len(s) - word_length + 1:
            if start == 0:
                current = s[:word_length]
            else:
                current = current[1:] + s[word_length - 1 + start]
            if matches(current, words):
                all_matches.append(start)
            start += 1
        return all_matches

s = Solution()
print(s.findSubstring("barfoothefoobarman", ["foo","bar"]))
print(s.findSubstring("wordgoodgoodgoodbestword", ["word","good","best","word"]))
print(s.findSubstring("barfoofoobarthefoobarman", ["bar","foo","the"]))
print(s.findSubstring("wordgoodgoodgoodbestword", ["word","good","best","good"]))