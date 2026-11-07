class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        # Create min heap of idle servers: (weight, server_index)
        # Servers with lower weight have higher priority
        idle_servers = [(weight, index) for index, weight in enumerate(servers)]
        heapify(idle_servers)
      
        # Min heap of busy servers: (available_time, weight, server_index)
        # Sorted by when they become available
        busy_servers = []
      
        # Result array to store which server handles each task
        result = []
      
        # Process each task at its arrival time
        for task_index, task_duration in enumerate(tasks):
            # Free up servers that have completed their tasks by current time
            while busy_servers and busy_servers[0][0] <= task_index:
                available_time, server_weight, server_index = heappop(busy_servers)
                heappush(idle_servers, (server_weight, server_index))
          
            # Assign task to an available server if one exists
            if idle_servers:
                server_weight, server_index = heappop(idle_servers)
                # Server will be busy until: current_time + task_duration
                heappush(busy_servers, (task_index + task_duration, server_weight, server_index))
            else:
                # No idle servers - wait for the earliest busy server to finish
                available_time, server_weight, server_index = heappop(busy_servers)
                # Server will be busy until: its_available_time + task_duration
                heappush(busy_servers, (available_time + task_duration, server_weight, server_index))
          
            # Record which server is handling this task
            result.append(server_index)
      
        return result
