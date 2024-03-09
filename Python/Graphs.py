#Q: Count the unique paths from the top left to the bottom right. A single path may only move along 0's and can't visit the same cell more than once.
#This is not optimal from top left to bottom right
#DFS APPROACH using Recursion
class solution:
seen = set()    
ROWS = len(grid)
COLS = len(grid[0])


    def helper(grid, r,c):
        if (row < 0 or c < 0 or r ==ROWS or c == COLS or (r,c) in seen or grid[r][c]==1):
            return 0 # edge cases
        
        if r == ROWS -1 and c == COLS -1:
            return 1 # if it reaches the end, we found the path
        
        seen.add((r,c))
        count = 0
        count += helper(grid, r+1,c)
        count += helper(grid, r-1,c)
        count += helper(grid, r, c+1)
        count += helper(grid, r, c-1)
        seen.remove((r,c))
        return count
    helper(grid,0,0)
                
        
#BFS APPROACH using Queue
from collections import deque
class solution:
    ROWS = len(grid) #length of rows
    COLS = len(grid[0]) #length of columns
    seen = set() #creating a hashset, so I don't revisit the same value
    queue = deque()
    queue.append((0,0)) #adding initial value to the queue
    visit.add((0,0)) #adding initial values
    
    
    length = 0 #keeping count of the length
    while queue is not None:
        for i in range(len(queue)):
            r,c = queue.popleft()
            if r == ROWS - 1 and c == COLS -1: #if the coordinates are at the end of row and column, that's the result
                return length #return length
            
            neighbors = [[0,1], [0,-1], [1,0] [-1,0]]
            for dr, dc in neighbors:
                if (r+dr < 0 or c+dc < 0 or r+dr == ROWS or c+dc == COLS or (r+dr, c+dc) in seen or grid[r+dr][c+dc]==1):
                    continue
                else:
                    queue.append((r+dr, c+dc))
                    seen.add((r+dr, c+dc))
        length +=1
        
# 200. Number of Islands
# https://leetcode.com/problems/number-of-islands/description/

from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Check if the grid is None
        if grid is None:
            return 0
        
        # Initialize a deque for breadth-first search
        queue = deque()
        
        # Initialize a counter for islands
        islands = 0
        
        # Set to keep track of visited cells
        seen = set()
        
        # Get the number of rows and columns in the grid
        ROWS = len(grid)
        COLS = len(grid[0])
        
        # Define a breadth-first search function
        def bfs(r,c):
            # Add the starting cell to the queue and mark it as seen
            queue.append((r,c))
            seen.add((r,c))
            
            # Iterate until the queue is empty
            while queue:
                # Dequeue a cell
                r,c = queue.popleft()
                
                # Define directions to explore: up, down, left, right
                directions = [[1,0], [-1,0], [0,1], [0,-1]]
                
                # Iterate over the directions
                for dr, dc in directions:
                    # Check if the new cell is out of bounds or already visited
                    if (dr+r<0 or dc+c<0 or dr+r == ROWS or dc+c == COLS or grid[dr+r][dc+c]=="0" or (dr+r, dc+c) in seen):
                        continue
                    else:
                        # Add the new cell to the queue and mark it as seen
                        queue.append((dr+r, dc+c))
                        seen.add((dr+r, dc+c))
        
        # Iterate through each cell in the grid
        for r in range(ROWS):
            for c in range(COLS):
                # If the cell is part of an unvisited island, perform BFS
                if grid[r][c]=="1" and (r,c) not in seen:
                    bfs(r,c)
                    # Increment the island counter
                    islands +=1
        
        # Return the total number of islands
        return islands

    
# 133. Clone Graph
# https://leetcode.com/problems/clone-graph/description/

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # Check if the input node is None
        if node is None:
            return None
        
        # Dictionary to map old nodes to their corresponding new copies
        oldToNew = {}

        # Depth-first search function to clone the graph
        def dfs(node):
            # If the node has already been cloned, return its copy
            if node in oldToNew:
                return oldToNew[node]
            else:
                # Create a new copy of the current node
                copy = Node(node.val)

                # Store the mapping of old node to new node copy
                oldToNew[node] = copy

                # Recursively clone the neighbors of the current node
                for nei in node.neighbors:
                    copy.neighbors.append(dfs(nei))
                
                # Return the copied node
                return copy
        
        # Start the depth-first search from the input node
        return dfs(node)

            
        
# 695. Max Area of Island
# https://leetcode.com/problems/max-area-of-island/description/

from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if grid is None:  # Check if the grid is None
            return 0

        result = 0  # Variable to store the maximum area of an island
        ROWS = len(grid)  # Number of rows in the grid
        COLS = len(grid[0])  # Number of columns in the grid
        queue = deque()  # Queue for BFS traversal
        seen = set()  # Set to keep track of visited cells

        def bfs(r, c):
            # Function to perform Breadth-First Search (BFS)
            queue.append((r, c))  # Add the starting cell to the queue
            seen.add((r, c))  # Mark the starting cell as visited
            area = 1  # Initialize the area of the island to 1

            # Perform BFS traversal
            while queue:
                r, c = queue.popleft()  # Get the next cell from the queue
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]  # Possible directions to move

                # Check each direction
                for dr, dc in directions:
                    if (r + dr < 0 or c + dc < 0 or r + dr == ROWS or c + dc == COLS or
                            grid[r + dr][c + dc] == 0 or (r + dr, c + dc) in seen):
                        # If the next cell is out of bounds, water, or already visited, skip it
                        continue
                    else:
                        queue.append((r + dr, c + dc))  # Add the next cell to the queue
                        seen.add((r + dr, c + dc))  # Mark the next cell as visited
                        area += 1  # Increment the area of the island

            return area  # Return the area of the island found by BFS

        # Iterate through each cell in the grid
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r, c) not in seen:
                    # If the cell represents land and has not been visited yet
                    result = max(result, bfs(r, c))  # Find the maximum area of the island

        return result  # Return the maximum area of an island in the grid


# 463. Island Perimeter
# https://leetcode.com/problems/island-perimeter/description/


from collections import deque

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        if grid is None:  # Check if the grid is None
            return None

        ROWS = len(grid)  # Number of rows in the grid
        COLS = len(grid[0])  # Number of columns in the grid
        seen = set()  # Set to keep track of visited cells
        queue = deque()  # Queue for BFS traversal
        result = 0  # Variable to store the perimeter

        def bfs(r, c):
            # Function to perform Breadth-First Search (BFS)
            queue.append((r, c))  # Add the starting cell to the queue
            seen.add((r, c))  # Mark the starting cell as visited
            peri = 0  # Initialize the perimeter of the island to 0

            # Perform BFS traversal
            while queue:
                r, c = queue.popleft()  # Get the next cell from the queue
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]  # Possible directions to move

                # Check each direction
                for dr, dc in directions:
                    if (dr + r < 0 or dc + c < 0 or dr + r == ROWS or dc + c == COLS or
                            grid[dr + r][dc + c] == 0):
                        # If the next cell is out of bounds or water, increment perimeter
                        peri += 1
                    elif (dr + r, dc + c) not in seen:
                        queue.append((dr + r, dc + c))  # Add the next cell to the queue
                        seen.add((dr + r, dc + c))  # Mark the next cell as visited

            return peri  # Return the perimeter of the island

        # Iterate through each cell in the grid
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) not in seen and grid[r][c] == 1:
                    # If the cell represents land and has not been visited yet
                    result += bfs(r, c)  # Find the perimeter of the island

        return result  # Return the total perimeter
