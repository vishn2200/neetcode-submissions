class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        def possible(start):
            tank = gas[start]
            if start+1 == n:
                i = 0
            else:
                i = start + 1
            while i!=start:
                if tank < cost[i-1]:
                    return False 
                else:
                    tank = tank - cost[i-1] + gas[i]
                    if i == n-1:
                        i = 0
                    else:
                        i+=1
            if tank < cost[i-1]:
                return False
            return True


        for i in range(n):
            
            if possible(i):
                return i
        return -1