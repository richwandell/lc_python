class Solution:
    def convert(self, s: str, numRows: int) -> str:
        n = len(s)
        i = 0
        tmp1 = []
        cols = []
        while i < n:
            if len(tmp1) == numRows:
                cols.append(tmp1)
                tmp2i = numRows - 2
                for j in range(numRows - 2):
                    col = ["" for _ in range(numRows)]
                    col[tmp2i] = s[i]
                    cols.append(col)
                    tmp2i -= 1
                    i += 1
                    if i == n:
                        break
                tmp1 = []
            else:
                tmp1.append(s[i])
                i += 1
        if len(tmp1) > 0:
            cols.append(tmp1)
        new_string = ""
        for i in range(numRows):
            for j in range(len(cols)):
                if len(cols[j]) > i and cols[j][i] != '':
                    new_string += cols[j][i]
        return new_string


s = Solution()
out1 = s.convert("PAYPALISHIRING", 4)
out2 = s.convert("ABCDE", 4)

print(out1, out2)

# 3 = 1
# 4 = 2
# 5 = 3
# 6 = 4