class Solution:
    def countServers(
        self, n: int, logs: List[List[int]], x: int, queries: List[int]
    ) -> List[int]:
        from collections import Counter
        from itertools import count
        from typing import List
      
        # Counter to track active servers in current window
        server_count = Counter()
      
        # Sort logs by timestamp for efficient window processing
        logs.sort(key=lambda log: log[1])
      
        # Initialize result array with same length as queries
        result = [0] * len(queries)
      
        # Two pointers for sliding window technique
        left_pointer = 0   # Points to the start of the current window
        right_pointer = 0  # Points to the end of the current window
      
        # Process queries in sorted order while maintaining original indices
        # zip(queries, count()) pairs each query with its original index
        for query_time, original_index in sorted(zip(queries, count())):
            # Calculate window boundaries
            window_start = query_time - x
            window_end = query_time
          
            # Expand window right: add all logs with timestamp <= window_end
            while right_pointer < len(logs) and logs[right_pointer][1] <= window_end:
                server_id = logs[right_pointer][0]
                server_count[server_id] += 1
                right_pointer += 1
          
            # Shrink window left: remove all logs with timestamp < window_start
            while left_pointer < len(logs) and logs[left_pointer][1] < window_start:
                server_id = logs[left_pointer][0]
                server_count[server_id] -= 1
                # Remove server from counter if count reaches 0
                if server_count[server_id] == 0:
                    server_count.pop(server_id)
                left_pointer += 1
          
            # Calculate servers with no requests (total servers - active servers)
            result[original_index] = n - len(server_count)
      
        return result
