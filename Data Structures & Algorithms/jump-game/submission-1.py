class Solution:
    def canJump(self, nums: List[int]) -> bool:
        furthest = 0
        n = len(nums)
        for i in range(n):
            if i <= furthest:
                furthest = max(furthest,i + nums[i])
            else:
                return False
        return True

        