class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        # Get dimensions of the grid
        rows, cols = len(grid), len(grid[0])
      
        # Count servers in each row and column
        row_counts = [0] * rows
        col_counts = [0] * cols
      
        # First pass: count servers in each row and column
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    row_counts[i] += 1
                    col_counts[j] += 1
      
        # Second pass: count servers that can communicate
        # A server can communicate if there's at least one other server
        # in the same row or column
        connected_servers = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and (row_counts[i] > 1 or col_counts[j] > 1):
                    connected_servers += 1
      
        return connected_servers
