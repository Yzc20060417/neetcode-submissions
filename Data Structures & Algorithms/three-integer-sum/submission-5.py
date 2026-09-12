class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        for i in range(len(nums)-2):
            x = nums[i]
            if i >0 and x == nums[i-1]:
                continue
            if x + nums[i+1] + nums[i+2] > 0:
                break
            if x + nums[-2] + nums[-1] < 0:
                continue
            l = i+1
            r = len(nums)-1
            while l<r:
                s = x + nums[l] + nums[r]
                if s > 0:
                    r -= 1
                elif s < 0:
                    l += 1
                else:
                    ans.append([x,nums[l],nums[r]])
                    l += 1
                    if nums[l] == nums[l-1]:
                        l += 1
                    r -= 1
                    if nums[r] == nums[r+1]:
                        r -= 1
        return ans
                
