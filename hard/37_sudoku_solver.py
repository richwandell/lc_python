from typing import List
import pprint


class Solution:

    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        our choice
        our constraints
        our goal
        """

        nums = list([str(n) for n in range(1, 10)])

        def can_place(r, c, n):
            can_place = False
            # check row
            if n not in board[r]:
                can_place = True
                # check col
                for i in range(len(board)):
                    if board[i][c] == n:
                        can_place = False
                        break
            if can_place:
                # validate sub grid
                if c < 3:
                    grid_x = 0
                elif c < 6:
                    grid_x = 1
                else:
                    grid_x = 2
                if r < 3:
                    grid_y = 0
                elif r < 6:
                    grid_y = 1
                else:
                    grid_y = 2
                for y in range(grid_y * 3, grid_y * 3 + 3):
                    for x in range(grid_x * 3, grid_x * 3 + 3):
                        if board[y][x] == n:
                            can_place = False
                            break
                    if not can_place:
                        break

                if can_place:
                    return True
            return False

        def solve(r, c):
            if c == len(board[0]):
                c = 0
                r += 1
                if r == len(board):
                    return True

            if board[r][c] != ".":
                return solve(r, c+1)

            for n in nums:
                if can_place(r, c, n):
                    board[r][c] = n
                    if solve(r, c+1):
                        return True
                    board[r][c] = "."
            return False
        solve(0, 0)





board = [
    ["5", "3", ".",   ".", "7", ".",   ".", ".", "."],
    ["6", ".", ".",   "1", "9", "5",   ".", ".", "."],
    [".", "9", "8",   ".", ".", ".",   ".", "6", "."],

    ["8", ".", ".",   ".", "6", ".",   ".", ".", "3"],
    ["4", ".", ".",   "8", ".", "3",   ".", ".", "1"],
    ["7", ".", ".",   ".", "2", ".",   ".", ".", "6"],

    [".", "6", ".",   ".", ".", ".",   "2", "8", "."],
    [".", ".", ".",   "4", "1", "9",   ".", ".", "5"],
    [".", ".", ".",   ".", "8", ".",   ".", "7", "9"]
]

s = Solution()
s.solveSudoku(board)
pprint.pprint(board)
