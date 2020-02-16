from typing import List
import pprint


class Solution:
    """
    board is a bitfield holding bits that indicate whether or not a queen is placed at a position
    - queens are placed by shifting 1 into place and using logical or board = board | (1 << (r*n+c))
    - queens are removed using a bit mask, shifting 1 into place, flipping all bits, and using & operator board = board & ~(1 << (r * n + c))

    bcols, bldiag, and brdiag are bitfields that represent whether a queen has been place in a column,
    the left diagonal, or the right diagonal. We can check these bitfields by shifting 1 and masking each value.
    Then we can use logical or with all three fields and check if the value is greater than 1. When a queen is
    added to a position we place the queen by shifting 1 and setting the field using logical or. When a queen is
    removed we mask the bit off of the bitfield.

    current: As paths are exhausted we save exhausted paths into a path cache using a python dictionary. The current path
    is a bitfield that is shifted "n" times for each row. The queen position in each row is added using logical or.
    current = (current << n) | c
    """

    def solveNQueens(self, n: int) -> List[List[str]]:

        def solve(r):

            nonlocal board, bcols, bldiag, brdiag, current

            for c in range(n):
                if bcols & (1 << c) | bldiag & (1 << (r - c + n)) | brdiag & (1 << (r + c)) < 1:
                    last_path = current

                    if current == 0:
                        current = 1

                    current = (current << n) | c

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