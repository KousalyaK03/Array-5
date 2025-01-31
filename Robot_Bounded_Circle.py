class Solution:
    # Approach:
    # - The robot is bounded in a circle if:
    #   1. It returns to the origin after one cycle of instructions.
    #   2. It does not face north at the end of the instructions (ensuring it will eventually return).
    # - We simulate the robot's movements using (x, y) coordinates and track direction using an index in a predefined directions list.
    def isRobotBounded(self, instructions: str) -> bool:
        # Directions in order: North, East, South, West (clockwise)
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        # Initialize robot's position and direction index (starts facing North)
        x, y = 0, 0
        direction_idx = 0  # 0: North, 1: East, 2: South, 3: West
        
        # Process each instruction
        for instruction in instructions:
            if instruction == 'G':  # Move forward in the current direction
                dx, dy = directions[direction_idx]
                x += dx
                y += dy
            elif instruction == 'L':  # Turn left (counter-clockwise)
                direction_idx = (direction_idx - 1) % 4
            elif instruction == 'R':  # Turn right (clockwise)
                direction_idx = (direction_idx + 1) % 4

        # The robot is bounded if it returns to the origin OR it does not face North
        return (x == 0 and y == 0) or direction_idx != 0

# Time Complexity: O(N) where N is the length of instructions.
#     - We process each character in the instructions once.
# Space Complexity: O(1) 
#     - We only store a few integer variables (x, y, direction_idx).
# Example usage
solution = Solution()
print(solution.isRobotBounded("GGLLGG"))  # Output: True
print(solution.isRobotBounded("GG"))      # Output: False
print(solution.isRobotBounded("GL"))      # Output: True