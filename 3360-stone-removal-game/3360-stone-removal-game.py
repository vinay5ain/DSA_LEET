class Solution:
    def canAliceWin(self, n: int) -> bool:
        
        stones_to_remove = 10
      
        total_turns = 0
      
        while n >= stones_to_remove:
           
            n -= stones_to_remove
       
            stones_to_remove -= 1
        
            total_turns += 1
        return total_turns % 2 == 1
