from typing import List
import pprint


class Solution:

    def solveNQueens(self, n: int) -> List[List[str]]:

        def solve(r):
            nonlocal board, bcols, bldiag, brdiag, current

            for c in range(n):
                if bcols & (1 << c) | bldiag & (1 << (r - c + n)) | brdiag & (1 << (r + c)) < 1:
                    last_path = current

                    if current == 0:
                        current = 1

                    current = (current << 4) | c

                    if current in exhausted_paths:
                        current = last_path
                        continue

                    board = board | (1 << (r*n+c))

                    lldiag, lrdiag = r-c + n, r+c
                    bcols, bldiag, brdiag = bcols | (1 << c), bldiag | (1 << lldiag), brdiag | (1 << lrdiag)

                    if r+1 == n or solve(r+1):
                        exhausted_paths[current] = False
                        return True

                    board = board & ~(1 << (r * n + c))
                    current = last_path

                    bcols, bldiag, brdiag = bcols & ~(1 << c), bldiag & ~(1 << lldiag), brdiag & ~(1 << lrdiag)

            exhausted_paths[current] = False
            return False

        boards, exhausted_paths = [], {}
        while True:
            board = 0
            bcols, bldiag, brdiag, current = 0, 0, 0, 0
            solve(0)
            if board > 0:
                new_board = []
                for r in range(n):
                    for c in range(n):
                        if board & (1 << r*n+c) > 0:
                            new_board.append(("." * c) + "Q" + ("." * (n - c - 1)))
                            break
                boards.append(new_board)
            else:
                break
        return boards


s = Solution()
boards = s.solveNQueens(9)

print(len(boards))
# pprint.pprint(boards, width=10)