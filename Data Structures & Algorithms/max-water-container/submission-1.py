class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        res = 0
        while l<r:
            temp = min(heights[l], heights[r])*(r-l)
            if temp > res:
                res = temp


            if heights[r] > heights[l]:
                l += 1
            elif heights[l] > heights[r]:
                r -= 1
            else:
                l+=1
                r-=1
        return res
        