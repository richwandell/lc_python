from typing import List
import pprint


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        used, boards, board, current = {}, [], [], []
        test_cache = {}
        bcols, bldiag, brdiag = 0, 0, 0

        def can_place_queen(r, c):
            mask = 1 << c
            t = bcols & mask
            if t > 0:
                return False
            mask = 1 << (abs(r-c))
            t = bldiag & mask
            if t > 0:
                return False

            mask = 1 << (r+c)
            t = brdiag & mask
            if t > 0:
                return False
            return True
            # lldiag = str(r-c)
            # lrdiag = str(r+c)
            # if c in cols or \
            #         lldiag in ldiag or lrdiag in rdiag:
            #     return False
            # return True

        def solve(r):
            nonlocal bcols, bldiag, brdiag
            if r == n:
                key = tuple(current)
                if key in used:
                    return False
                bcols, bldiag, brdiag = 0, 0, 0
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

                    lldiag = abs(r-c)
                    lrdiag = r+c

                    bcols = bcols | (1 << c)
                    bldiag = bldiag | (1 << lldiag)
                    brdiag = brdiag | (1 << lrdiag)

                    if solve(r+1):
                        return True
                    board[r][c] = "."
                    last = current.pop()
                    mask = ~(1 << c)
                    bcols = bcols & mask

                    mask = ~(1 << lldiag)
                    bldiag = bldiag & mask

                    mask = ~(1 << lrdiag)
                    brdiag = brdiag & mask

            test_cache[cache_key] = False
            return False

        row = ["." for _ in range(n)]
        while True:
            current = []
            board = [list(row) for _ in range(n)]
            bcols, bldiag, brdiag = 0, 0, 0
            solve(0)
            if "Q" in board[0]:
                board = ["".join(x) for x in board]
                boards.append(board)
            else:
                break
        return boards


s = Solution()
boards = s.solveNQueens(4)

print(len(boards))
pprint.pprint(boards, width=10)