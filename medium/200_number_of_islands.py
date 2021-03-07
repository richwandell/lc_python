from typing import List


class Solution:
    """
    Given an m x n 2d grid map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
You may assume all four edges of the grid are all surrounded by water.

    """
    def numIslands(self, grid: List[List[str]]) -> int:
        if len(grid) == 0: return 0

        def get_local_land(r, c):
            nonlocal grid

            land = []
            if r - 1 > -1 and grid[r-1][c] == "1":
                land.append((r-1, c))
            if r + 1 < len(grid) and grid[r+1][c] == "1":
                land.append((r+1, c))
            if c - 1 > -1 and  grid[r][c-1] == "1":
                land.append((r, c-1))
            if c + 1 < len(grid[0]) and  grid[r][c+1] == "1":
                land.append((r, c+1))
            return land

        all_land = {}
        island_num = 0
        stack = []

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if (r, c) in all_land:
                    continue

                if grid[r][c] == "0":
                    continue

                island_num += 1
                all_land[(r, c)] = island_num

                stack.append((r, c))
                while len(stack) > 0:
                    item = stack.pop()
                    local_land = get_local_land(item[0], item[1])
                    for land in local_land:
                        if land not in all_land:
                            stack.append(land)
                            all_land[land] = island_num

        return len(set(all_land.values()))

s = Solution()
print(s.numIslands([
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]))

print(s.numIslands([
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]))