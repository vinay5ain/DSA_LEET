class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        """
        Find all indices of target value in sorted array.

        Args:
            nums: List of integers to search through
            target: The target value to find indices for

        Returns:
            List of indices where target appears in the sorted array
        """
        # Sort the array in ascending order (modifies in-place)
        nums.sort()

        # Use list comprehension to collect all indices where value equals target
        # enumerate() provides (index, value) pairs for each element
        result = [i for i, v in enumerate(nums) if v == target]

        return result
