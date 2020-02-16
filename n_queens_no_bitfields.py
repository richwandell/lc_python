from typing import List
import pprint


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        used, boards, board, current = {}, [], [], []
        test_cache = {}
        rows, cols, ldiag, rdiag = {}, {}, {}, {}

        def can_place_queen(r, c):
            lldiag = str(r-c)
            lrdiag = str(r+c)
            if r in rows or c in cols or \
                    lldiag in ldiag or lrdiag in rdiag:
                return False
            return True

        def solve(r):
            nonlocal rows, cols, ldiag, rdiag
            if r == n:
                key = tuple(current)
                if key in used:
                    return False
                rows, cols, ldiag, rdiag = {}, {}, {}, {}
                used[key] = True
                return True

            cache_key = tuple(current)
            if cache_key in test_cache:
                if not test_cache[cache_key]:
                    return False

            for c in range(n):
                if can_place_queen(r, c):
                    current.append((r, c))
                    board[r][c] = "Q"
                    rows[r] = True
                    cols[c] = True

                    lldiag = str(r-c)
                    lrdiag = str(r+c)
                    ldiag[lldiag] = True
                    rdiag[lrdiag] = True

                    if solve(r+1):
                        return True
                    board[r][c] = "."
                    last = current.pop()
                    del rows[last[0]]
                    del cols[last[1]]
                    del ldiag[lldiag]
                    del rdiag[lrdiag]
            test_cache[cache_key] = False
            return False

        row = ["." for _ in range(n)]
        while True:
            current = []
            board = [list(row) for _ in range(n)]
            rows, cols, ldiag, rdiag = {}, {}, {}, {}
            solve(0)
            if "Q" in board[0]:
                board = ["".join(x) for x in board]
                boards.append(board)
            else:
                break
        return boards


s = Solution()
boards = s.solveNQueens(9)

print(len(boards))
pprint.pprint(boards, width=10)