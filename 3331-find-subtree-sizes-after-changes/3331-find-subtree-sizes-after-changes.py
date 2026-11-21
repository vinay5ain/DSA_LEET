from typing import List
from collections import defaultdict

class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        """
        Find the size of subtrees for each node in a tree with special character-based rules.
      
        Args:
            parent: List where parent[i] is the parent of node i (parent[0] = -1 for root)
            s: String where s[i] is the character associated with node i
      
        Returns:
            List where result[i] is the subtree size for node i
        """
      
        def dfs(node: int, parent_node: int) -> None:
            """
            Depth-first search to calculate subtree sizes.
          
            Args:
                node: Current node being processed
                parent_node: Parent of the current node (-1 for root)
            """
            # Initialize the subtree size for current node
            subtree_sizes[node] = 1
          
            # Add current node to the stack of nodes with the same character
            char_stack[s[node]].append(node)
          
            # Process all children of the current node
            for child in adjacency_list[node]:
                dfs(child, node)
          
            # Determine which ancestor should receive this subtree's size
            target_ancestor = parent_node
          
            # If there are multiple nodes with the same character in the path,
            # use the second-to-last one (the previous occurrence)
            if len(char_stack[s[node]]) > 1:
                target_ancestor = char_stack[s[node]][-2]
          
            # Add current subtree size to the target ancestor
            if target_ancestor != -1:
                subtree_sizes[target_ancestor] += subtree_sizes[node]
          
            # Remove current node from the character stack after processing
            char_stack[s[node]].pop()
      
        # Initialize variables
        n = len(s)
      
        # Build adjacency list representation of the tree
        adjacency_list = [[] for _ in range(n)]
        for i in range(1, n):
            adjacency_list[parent[i]].append(i)
      
        # Dictionary to track nodes with each character during DFS
        char_stack = defaultdict(list)
      
        # Initialize result array for subtree sizes
        subtree_sizes = [0] * n
      
        # Start DFS from root node (node 0)
        dfs(0, -1)
      
        return subtree_sizes
