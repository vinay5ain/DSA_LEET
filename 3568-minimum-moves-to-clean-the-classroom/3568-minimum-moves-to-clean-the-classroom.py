class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        # Get dimensions of the classroom
        rows, cols = len(classroom), len(classroom[0])
      
        # Create a 2D array to store lamp indices
        lamp_indices = [[0] * cols for _ in range(rows)]
      
        # Find starting position and count lamps
        start_row = start_col = lamp_count = 0
        for row_idx, row in enumerate(classroom):
            for col_idx, cell in enumerate(row):
                if cell == "S":
                    # Mark starting position
                    start_row, start_col = row_idx, col_idx
                elif cell == "L":
                    # Assign index to each lamp
                    lamp_indices[row_idx][col_idx] = lamp_count
                    lamp_count += 1
      
        # If no lamps to turn off, return 0
        if lamp_count == 0:
            return 0
      
        # Create 4D visited array: [row][col][energy_level][lamp_state_mask]
        visited = [
            [[[False] * (1 << lamp_count) for _ in range(energy + 1)] for _ in range(cols)]
            for _ in range(rows)
        ]
      
        # Initialize BFS queue with starting state
        # (row, col, current_energy, lamp_mask) where lamp_mask has all lamps on (all bits set to 1)
        queue = [(start_row, start_col, energy, (1 << lamp_count) - 1)]
        visited[start_row][start_col][energy][(1 << lamp_count) - 1] = True
      
        # Direction vectors for moving up, right, down, left
        directions = (-1, 0, 1, 0, -1)
      
        # Initialize move counter
        moves = 0
      
        # BFS to find minimum moves
        while queue:
            # Process all states at current level
            current_level = queue
            queue = []
          
            for current_row, current_col, current_energy, lamp_mask in current_level:
                # Check if all lamps are turned off
                if lamp_mask == 0:
                    return moves
              
                # Skip if no energy left
                if current_energy <= 0:
                    continue
              
                # Try moving in all 4 directions
                for direction_idx in range(4):
                    next_row = current_row + directions[direction_idx]
                    next_col = current_col + directions[direction_idx + 1]
                  
                    # Check if next position is valid and not a wall
                    if 0 <= next_row < rows and 0 <= next_col < cols and classroom[next_row][next_col] != "X":
                        # Calculate energy after move
                        # Restore to full energy if stepping on recharge station, otherwise decrease by 1
                        next_energy = (
                            energy if classroom[next_row][next_col] == "R" else current_energy - 1
                        )
                      
                        # Update lamp mask if stepping on a lamp
                        next_lamp_mask = lamp_mask
                        if classroom[next_row][next_col] == "L":
                            # Turn off the lamp by clearing its bit
                            next_lamp_mask &= ~(1 << lamp_indices[next_row][next_col])
                      
                        # Add to queue if this state hasn't been visited
                        if not visited[next_row][next_col][next_energy][next_lamp_mask]:
                            visited[next_row][next_col][next_energy][next_lamp_mask] = True
                            queue.append((next_row, next_col, next_energy, next_lamp_mask))
          
            # Increment move counter after processing current level
            moves += 1
      
        # Return -1 if impossible to turn off all lamps
        return -1