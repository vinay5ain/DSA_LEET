class Solution:
    def countDaysTogether(
        self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str
    ) -> int:
        """
        Calculate the number of days Alice and Bob are together.
      
        Args:
            arriveAlice: Alice's arrival date in "MM-DD" format
            leaveAlice: Alice's departure date in "MM-DD" format
            arriveBob: Bob's arrival date in "MM-DD" format
            leaveBob: Bob's departure date in "MM-DD" format
          
        Returns:
            Number of days both are present together
        """
        # Find the overlapping period
        # Latest arrival date (start of overlap)
        overlap_start = max(arriveAlice, arriveBob)
        # Earliest departure date (end of overlap)
        overlap_end = min(leaveAlice, leaveBob)
      
        # Days in each month (non-leap year)
        days_in_month = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
      
        # Convert start date to day of year
        # Extract month and day from "MM-DD" format
        start_month = int(overlap_start[:2])
        start_day = int(overlap_start[3:])
        # Calculate total days from January 1st to start date
        start_day_of_year = sum(days_in_month[:start_month - 1]) + start_day
      
        # Convert end date to day of year
        end_month = int(overlap_end[:2])
        end_day = int(overlap_end[3:])
        # Calculate total days from January 1st to end date
        end_day_of_year = sum(days_in_month[:end_month - 1]) + end_day
      
        # Calculate overlapping days (inclusive of both start and end)
        # If end is before start, there's no overlap, return 0
        return max(end_day_of_year - start_day_of_year + 1, 0)
