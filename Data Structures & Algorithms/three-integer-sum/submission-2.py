class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        triplets = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]: continue
            r = len(nums) -1
            l = i + 1
            x = nums[i]
            while r>l:
                y = nums[r]
                z = nums[l] 
                if y+z == -x:
                    triplets.append([x,y,z])
                    r -=1
                    l +=1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    # Skip identical values for the right pointer
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
                if y+z > -x:
                    r -=1
                if y+z < -x:
                    l += 1
        return triplets





