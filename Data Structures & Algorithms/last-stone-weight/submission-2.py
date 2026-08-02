class Solution:
    
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [i*-1 for i in stones]
        heapq.heapify(stones)
        while len(stones)>=2:
            x = heapq.heappop(stones)*-1
            y = heapq.heappop(stones)*-1
            if x != y:
                heapq.heappush(stones, abs(x-y)*-1)
        if stones:
            return stones[0] if stones[0] >0 else stones[0]*-1
        else:
            return 0
        
