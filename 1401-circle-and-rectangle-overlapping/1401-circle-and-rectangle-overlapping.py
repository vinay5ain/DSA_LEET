class Solution:
    def checkOverlap(
        self,
        radius: int,
        xCenter: int,
        yCenter: int,
        x1: int,
        y1: int,
        x2: int,
        y2: int,
    ) -> bool:
        """
        Check if a circle overlaps with an axis-aligned rectangle.
      
        Args:
            radius: Radius of the circle
            xCenter: X-coordinate of the circle's center
            yCenter: Y-coordinate of the circle's center
            x1: X-coordinate of the rectangle's bottom-left corner
            y1: Y-coordinate of the rectangle's bottom-left corner
            x2: X-coordinate of the rectangle's top-right corner
            y2: Y-coordinate of the rectangle's top-right corner
          
        Returns:
            True if the circle and rectangle overlap, False otherwise
        """
      
        def get_closest_distance_to_range(range_start: int, range_end: int, point: int) -> int:
            """
            Calculate the shortest distance from a point to a range [range_start, range_end].
          
            If the point is within the range, the distance is 0.
            If the point is outside the range, return the distance to the nearest boundary.
          
            Args:
                range_start: Start of the range (inclusive)
                range_end: End of the range (inclusive)
                point: The point to measure distance from
              
            Returns:
                The shortest distance from the point to the range
            """
            if range_start <= point <= range_end:
                # Point is within the range
                return 0
          
            if point < range_start:
                # Point is to the left/below the range
                return range_start - point
            else:
                # Point is to the right/above the range
                return point - range_end
      
        # Calculate the closest horizontal distance from circle center to rectangle
        horizontal_distance = get_closest_distance_to_range(x1, x2, xCenter)
      
        # Calculate the closest vertical distance from circle center to rectangle
        vertical_distance = get_closest_distance_to_range(y1, y2, yCenter)
      
        # Check if the squared distance is within the squared radius
        # Using squared values to avoid floating point operations
        squared_distance = horizontal_distance ** 2 + vertical_distance ** 2
        squared_radius = radius ** 2
      
        return squared_distance <= squared_radius
