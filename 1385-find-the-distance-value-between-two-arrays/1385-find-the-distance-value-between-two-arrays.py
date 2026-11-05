from typing import List
from bisect import bisect_left


class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        # Sort arr2 to enable binary search
        arr2.sort()

        # Initialize counter for valid elements
        distance_value_count = 0

        # Check each element in arr1
        for num in arr1:
            # Find the leftmost position where (num - d) could be inserted in arr2
            # This gives us the index of the smallest element >= (num - d)
            left_bound_index = bisect_left(arr2, num - d)

            # An element from arr1 is valid if:
            # 1. left_bound_index == len(arr2): all elements in arr2 are < (num - d)
            # 2. arr2[left_bound_index] > (num + d): the smallest element >= (num - d) is also > (num + d)
            # Both conditions mean no element in arr2 is within distance d from num
            is_valid = (left_bound_index == len(arr2) or arr2[left_bound_index] > num + d)
            distance_value_count += is_valid

        return distance_value_count
