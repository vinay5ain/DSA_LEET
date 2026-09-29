class Solution:
    def hasValidPath(self, grid: List[List[str]]) -> bool:
        from functools import cache
        from typing import List
      
        @cache
        def dfs(row: int, col: int, open_count: int) -> bool:
            """
            Depth-first search to find valid parentheses path.
          
            Args:
                row: Current row position
                col: Current column position
                open_count: Number of unmatched opening parentheses
          
            Returns:
                True if a valid path exists from current position to end
            """
            # Update open parentheses count based on current cell
            delta = 1 if grid[row][col] == "(" else -1
            open_count += delta
          
            # Pruning: invalid if negative count or impossible to balance
            if open_count < 0:
                return False
          
            # Maximum possible closing parentheses from current position to end
            remaining_steps = (rows - row - 1) + (cols - col - 1)
            if open_count > remaining_steps:
                return False
          
            # Check if we reached the destination
            if row == rows - 1 and col == cols - 1:
                return open_count == 0
          
            # Try moving right and down
            directions = [(0, 1), (1, 0)]  # right, down
            for dx, dy in directions:
                next_row, next_col = row + dx, col + dy
                # Check bounds and recursively explore
                if 0 <= next_row < rows and 0 <= next_col < cols:
                    if dfs(next_row, next_col, open_count):
                        return True
          
            return False
      
        rows, cols = len(grid), len(grid[0])
      
        # Early termination checks
        # Path length must be even for balanced parentheses
        if (rows + cols - 1) % 2 == 1:
            return False
      
        # Start must be '(' and end must be ')'
        if grid[0][0] == ")" or grid[rows - 1][cols - 1] == "(":
            return False
      
        # Start DFS from top-left corner with 0 open parentheses
        return dfs(0, 0, 0)
