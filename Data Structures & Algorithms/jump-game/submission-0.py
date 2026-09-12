class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [False]*n
        dp[0] = True
        for i in range(n):
            for j in range(i):
                if dp[j] == True and nums[j] + j >= i:
                    dp[i] = True
        return True if dp[n-1] is True else False


        