class Solution:
    def missingNumber(self, nums):
        
        dp = [False for _ in range(len(nums)+1)]
        
        for n in nums:
            dp[n] = True
            
        for i in range(len(dp)):
            if not dp[i]:
                return i
                
            
        return None