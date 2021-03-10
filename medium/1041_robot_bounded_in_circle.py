class Solution:
    """
    On an infinite plane, a robot initially stands at (0, 0) and faces north. The robot can receive one of three
    instructions:

"G": go straight 1 unit;
"L": turn 90 degrees to the left;
"R": turn 90 degrees to the right.
The robot performs the instructions given in order, and repeats them forever.

Return true if and only if there exists a circle in the plane such that the robot never leaves the circle.

Example 1:

Input: instructions = "GGLLGG"
Output: true
Explanation: The robot moves from (0,0) to (0,2), turns 180 degrees, and then returns to (0,0).
When repeating these instructions, the robot remains in the circle of radius 2 centered at the origin.
Example 2:

Input: instructions = "GG"
Output: false
Explanation: The robot moves north indefinitely.
Example 3:

Input: instructions = "GL"
Output: true
Explanation: The robot moves from (0, 0) -> (0, 1) -> (-1, 1) -> (-1, 0) -> (0, 0) -> ...
    """
    def isRobotBounded(self, instructions: str) -> bool:
        start, pos = [0, 0, 0], [0, 0, 0]

        for _ in range(4):
            for letter in instructions:
                if letter == "G":
                    if pos[2] == 0:
                        pos[1] = pos[1]+1
                    elif pos[2] == 1:
                        pos[0] = pos[0]+1
                    elif pos[2] == 2:
                        pos[1] = pos[1]-1
                    else:
                        pos[0] = pos[0]-1
                elif letter == "L":
                    pos[2] = (pos[2] - 1) % 4
                else:
                    pos[2] = (pos[2] + 1) % 4
        if start == pos:
            return True
        return False


s = Solution()
print(s.isRobotBounded("GGLLGG"))
print(s.isRobotBounded("GG"))
print(s.isRobotBounded("GL"))