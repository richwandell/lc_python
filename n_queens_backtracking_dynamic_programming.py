from typing import List
import pprint


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        used = {}
        boards = []
        board = []
        current = []
        place_cache = {}

        def can_place_queen(r, c):
            for q in current:
                if q[1] == c or abs(q[0] - r) == abs(q[1] - c):
                    return False
            return True

        def solve(r):

            if r == n:
                key = tuple(current)
                if key in used:
                    return False
                used[key] = True
                return True
            place_cache_key = tuple(current)
            if place_cache_key in place_cache:
                if place_cache[place_cache_key] == False:
                    return False
            for c in range(n):
                if can_place_queen(r, c):
                    current.append((r, c))
                    board[r][c] = "Q"
                    if solve(r+1):
                        return True
                    board[r][c] = "."
                    current.pop()
            place_cache[place_cache_key] = False
            return False

        row = ["." for _ in range(n)]
        while True:
            current = []
            board = [list(row) for _ in range(n)]
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