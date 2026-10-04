class Solution:
    def checkValidString(self, s: str) -> bool:
   
        n = len(s)
      
        
        dp = [[False] * n for _ in range(n)]
      
        for i, char in enumerate(s):
            dp[i][i] = (char == '*')
      
   
        for i in range(n - 2, -1, -1):
        
            for j in range(i + 1, n):
            
                is_matching_pair = (
                    s[i] in '(*' and 
                    s[j] in '*)' and 
                    (i + 1 == j or dp[i + 1][j - 1])
                )
              
          
           
                can_split = any(
                    dp[i][k] and dp[k + 1][j] 
                    for k in range(i, j)
                )
              
                dp[i][j] = is_matching_pair or can_split
      
        
        return dp[0][n - 1]
