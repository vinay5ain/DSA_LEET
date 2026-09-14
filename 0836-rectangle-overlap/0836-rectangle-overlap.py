from typing import List

class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
     
        # Extract coordinates for first rectangle
        x1, y1, x2, y2 = rec1
      
        # Extract coordinates for second rectangle  
        x3, y3, x4, y4 = rec2
      
   
        return not (y3 >= y2 or y4 <= y1 or x3 >= x2 or x4 <= x1)