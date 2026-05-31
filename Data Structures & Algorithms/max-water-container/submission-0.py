class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxv = 0
        l = 0
        r = len(heights) -1

        while l<r:
            print(l,r)
            minv = min(heights[l], heights[r])
            print(heights[l], heights[r])
            area = minv * (r-l)
            print(area)
            maxv = max(maxv, area)

            if minv == heights[l]:
                l+=1 

            if minv == heights[r]:
                r-=1 

            

        return maxv

                 




