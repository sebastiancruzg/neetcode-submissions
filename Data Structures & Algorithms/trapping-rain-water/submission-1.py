class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: return 0
        water = 0
        l = 0
        r = len(height) - 1 
        ml = height[l]
        mr = height[r]

        while l<r:

            if ml<mr:
                l += 1
                ml = max(ml, height[l])
                water += ml  - height[l]
            else:
                r -=1
                mr = max(mr, height[r])
                water += mr - height[r]

        return water