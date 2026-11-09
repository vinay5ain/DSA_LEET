class Solution:
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
        # Initialize a sorted list of available servers (0 to k-1)
        available_servers = SortedList(range(k))
      
        # Min heap to track busy servers: (end_time, server_id)
        busy_servers = []
      
        # Counter array to track number of requests handled by each server
        request_count = [0] * k
      
        # Process each request
        for request_id, (arrival_time, processing_time) in enumerate(zip(arrival, load)):
            # Free up servers that have completed their tasks by current arrival time
            while busy_servers and busy_servers[0][0] <= arrival_time:
                end_time, server_id = heappop(busy_servers)
                available_servers.add(server_id)
          
            # Skip this request if no servers are available
            if not available_servers:
                continue
          
            # Find the next available server using round-robin strategy
            # Start looking from server (request_id % k)
            target_server = request_id % k
            server_index = available_servers.bisect_left(target_server)
          
            # If no server >= target_server exists, wrap around to the first server
            if server_index == len(available_servers):
                server_index = 0
          
            # Assign the request to the selected server
            selected_server = available_servers[server_index]
            request_count[selected_server] += 1
          
            # Mark server as busy until arrival_time + processing_time
            heappush(busy_servers, (arrival_time + processing_time, selected_server))
            available_servers.remove(selected_server)
      
        # Find servers with maximum request count
        max_requests = max(request_count)
        return [server_id for server_id, count in enumerate(request_count) if count == max_requests]
