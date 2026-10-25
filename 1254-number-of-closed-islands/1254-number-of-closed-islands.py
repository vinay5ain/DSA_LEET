class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        """
        Count the number of closed islands in the grid.
        A closed island is an island totally surrounded by 1s (land) and 
        doesn't touch the grid boundary.
      
        Args:
            grid: 2D array where 0 represents land and 1 represents water
          
        Returns:
            Number of closed islands
        """
        def dfs(row: int, col: int) -> int:
            """
            Perform DFS to explore an island and check if it's closed.
          
            Args:
                row: Current row position
                col: Current column position
              
            Returns:
                1 if the island is closed (not touching boundary), 0 otherwise
            """
            # Check if current cell is not on the boundary (closed island condition)
            is_not_boundary = int(0 < row < rows - 1 and 0 < col < cols - 1)
          
            # Mark current cell as visited by setting it to 1 (water)
            grid[row][col] = 1
          
            # Explore all 4 directions (up, right, down, left)
            for i in range(4):
                next_row = row + directions[i]
                next_col = col + directions[i + 1]
              
                # If neighbor is within bounds and is land (0), continue DFS
                if 0 <= next_row < rows and 0 <= next_col < cols and grid[next_row][next_col] == 0:
                    # Use bitwise AND to ensure all connected cells are also not on boundary
                    is_not_boundary &= dfs(next_row, next_col)
          
            return is_not_boundary
      
        # Get grid dimensions
        rows, cols = len(grid), len(grid[0])
      
        # Direction vectors for moving up, right, down, left
        # Using the pattern: (row_offset, col_offset) pairs
        directions = [-1, 0, 1, 0, -1]
      
        # Count closed islands by checking each unvisited land cell
        closed_island_count = 0
        for row in range(rows):
            for col in range(cols):
                # If cell is land (0) and forms a closed island, increment count
                if grid[row][col] == 0 and dfs(row, col):
                    closed_island_count += 1
                  
        return closed_island_count
