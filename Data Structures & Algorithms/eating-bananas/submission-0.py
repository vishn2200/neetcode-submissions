class Solution:
    import math
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        for i in range(1, max(piles)+1):
            hours = 0
            flag = 0
            for j in piles:
                hours += math.ceil(j/i)
                if hours > h:
                    flag = 1
                    break
            if flag == 0:
                return i
          

        
        