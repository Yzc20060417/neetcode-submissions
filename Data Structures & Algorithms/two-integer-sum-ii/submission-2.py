class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers)-1
        while l < r:
            if numbers[l] + numbers[r] > target:
                r -= 1
                if numbers[r+1] == numbers[r]:
                    r += 1
            elif numbers[l] + numbers[r] < target:
                l += 1
                if numbers[l-1] == numbers[l]:
                    l += 1
            else:
                return [l+1,r+1]