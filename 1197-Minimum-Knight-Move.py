# In an infinite chess board with coordinates from -infinity to +infinity, you have a knight at square [0, 0].

# A knight has 8 possible moves it can make, as illustrated below. Each move is two squares in a cardinal direction, then one square in an orthogonal direction.

# Return the minimum number of steps needed to move the knight to the square [x, y]. It is guaranteed the answer exists.

# Example 1:

# Input: x = 2, y = 1
# Output: 1

# Explanation: [0, 0] → [2, 1]
# Example 2:

# Input: x = 5, y = 5
# Output: 4

from collections import deque


def minKnightMoves(self, x: int, y: int) -> int:
    directions = [(1, 2), (-1, 2), (2, 1), (2, -1), (-1, -2), (1, -2), (-2, 1), (-2, -1)]

    def bfs(x, y):
        visted = set()
        queue = deque([(0, 0)])
        steps = 0

        while queue:
            cnt = len(queue)

            for i in range(cnt):
                currX, currY = queue.popleft()

                if (currX, currY) == (x, y):
                    return steps
                
                for dx, dy in directions:
                    newX, newY = currX + dx, currY + dy
                    
                    if (newX, newY) not in visted:
                        visted.add((newX, newY))
                        queue.append((newX, newY))

            steps += 1

    return bfs(x, y)
