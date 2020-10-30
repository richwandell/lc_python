class Solution:
    def romanToInt(self, s: str) -> int:
        vals = {
            'I': 1,
            'IV': 4,
            'V': 5,
            'IX': 9,
            'X': 10,
            'XL': 40,
            'L': 50,
            'XC': 90,
            'C': 100,
            'CD': 400,
            'D': 500,
            'CM': 900,
            'M': 1000
        }
        i, sl, total = 0, len(s), 0
        while i < sl:
            if i + 1 < sl:
                a = s[i:i+2]
                if a in vals:
                    total += vals[a]
                    i += 2
                    continue
            total += vals[s[i]]
            i += 1
        return total


s = Solution()
assert s.romanToInt('I') == 1
assert s.romanToInt('V') == 5
assert s.romanToInt('X') == 10
assert s.romanToInt('L') == 50
assert s.romanToInt('C') == 100
assert s.romanToInt('D') == 500
assert s.romanToInt('M') == 1000
assert s.romanToInt('III') == 3
assert s.romanToInt("IV") == 4
assert s.romanToInt("IX") == 9
assert s.romanToInt("MCMXCIV") == 1994