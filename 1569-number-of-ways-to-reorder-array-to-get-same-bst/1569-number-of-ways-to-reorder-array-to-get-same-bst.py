class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        def count_bst_permutations(arr):
            """
            Count the number of permutations that produce the same BST structure.
          
            Args:
                arr: Current array/subtree to process
          
            Returns:
                Number of valid permutations for this subtree
            """
            # Base case: arrays with less than 2 elements have only 1 permutation
            if len(arr) < 2:
                return 1
          
            # Split array into left and right subtrees based on first element (root)
            root = arr[0]
            left_subtree = [x for x in arr if x < root]
            right_subtree = [x for x in arr if x > root]
          
            # Get sizes of left and right subtrees
            left_size = len(left_subtree)
            right_size = len(right_subtree)
          
            # Recursively count permutations for left and right subtrees
            left_permutations = count_bst_permutations(left_subtree)
            right_permutations = count_bst_permutations(right_subtree)
          
            # Calculate total permutations using combinations
            # C(left_size + right_size, left_size) represents ways to interleave
            # left and right subtree elements while maintaining their relative order
            total_size = left_size + right_size
            combinations = binomial_coefficients[total_size][left_size]
          
            # Total permutations = combinations * left_permutations * right_permutations
            result = (combinations * left_permutations % MOD) * right_permutations % MOD
            return result
      
        # Initialize constants
        n = len(nums)
        MOD = 10**9 + 7
      
        # Precompute binomial coefficients using Pascal's triangle
        # binomial_coefficients[i][j] represents C(i, j) = i! / (j! * (i-j)!)
        binomial_coefficients = [[0] * n for _ in range(n)]
        binomial_coefficients[0][0] = 1
      
        for i in range(1, n):
            binomial_coefficients[i][0] = 1  # C(i, 0) = 1
            for j in range(1, i + 1):
                # Pascal's triangle formula: C(i, j) = C(i-1, j) + C(i-1, j-1)
                binomial_coefficients[i][j] = (
                    binomial_coefficients[i - 1][j] + 
                    binomial_coefficients[i - 1][j - 1]
                ) % MOD
      
        # Calculate total permutations and subtract 1 (excluding original arrangement)
        total_permutations = count_bst_permutations(nums)
        return (total_permutations - 1 + MOD) % MOD
