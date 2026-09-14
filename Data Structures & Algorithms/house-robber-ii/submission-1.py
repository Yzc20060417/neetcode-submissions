class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        dp1 = [0] * (n-1)
        dp2 = [0] * (n-1)
        dp1[0] = nums[0]
        dp2[0] = nums[1]
        for i in range(1, n-1):
            dp1[i] = max(dp1[i-1],dp1[i-2]+nums[i])
        for j in range(2, n):
            dp2[j-1] = max(dp2[j-2],dp2[j-3]+nums[j])
        return max(dp1[n-2],dp2[n-2])

        