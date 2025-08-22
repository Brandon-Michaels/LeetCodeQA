# Problem Summary:
# Given nxn matrix / grid, 1 represents land, 0 represents water
# island is 4-directionally connected group of 1's, not diagonally connected
# TWO ISLANDS IN GRID, no more no less
# connect in shortest manner, and return number of 0's needed to flip

# Approach:
# DFS approach, we can simply traverse the grid in search of land, 
# create a DFS function that finds distance from one land to next land
# you don't want to visit water and then return to same island, so prob want to
# keep visited set or some marker so we only track distance between islands, and don't
# by mistake return to the same island and say that is the min distance
# may have to run DFS a few times to reach island from optimal square
# dfs on one island and mark cells as visited, that way we don't return to that island
# bridge forwards/backwards will be the same distance, so let's just do it one way
# Time-Complexity: O(grid * n)
# Space-Complexity: O(grid)

# Optimal Approach:
# Easier to use BFS, your frontier (queue) should hold cells that border water
# so if an island cell borders water we can run BFS to other island from that cell
# If you are ever doing shortest path problems, can you can't use Djikstra's BFS IS THE WAY TO GO
# DFS often finds long, meandering path, BFS goes level by level, so will find the optimal path
# so immediately should've been BFS on this problem

from collections import deque

class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n = len(grid)
        first_island = []
        
        # 1. DFS to find and mark the first island
        def dfs_island(x, y):
            if not (0 <= x < n and 0 <= y < n and grid[x][y] == 1):
                return
            
            grid[x][y] = 2  # Mark as part of the first island
            first_island.append((x, y))
            
            dfs_island(x + 1, y)
            dfs_island(x - 1, y)
            dfs_island(x, y + 1)
            dfs_island(x, y - 1)

        # Find the starting point for the DFS
        found_island = False
        for x in range(n):
            for y in range(n):
                if grid[x][y] == 1:
                    dfs_island(x, y)
                    found_island = True
                    break
            if found_island:
                break
        
        # 2. BFS to find the shortest bridge
        queue = deque(first_island)
        distance = 0
        
        while queue:
            level_size = len(queue)
            for _ in range(level_size):
                x, y = queue.popleft()
                
                # Check neighbors
                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nx, ny = x + dx, y + dy
                    
                    if 0 <= nx < n and 0 <= ny < n:
                        if grid[nx][ny] == 1:
                            return distance
                        if grid[nx][ny] == 0:
                            grid[nx][ny] = -1 # Mark visited water
                            queue.append((nx, ny))
            distance += 1
        
        return -1 # Should not be reached given the problem constraints
