class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return 
        n = len(nums)
        res = []
        sol = []
        def dfs():
            for i in nums:
                if len(sol) == n:
                    res.append(sol[:])
                    return
                if i in sol:
                    continue
                else:
                    sol.append(i)
                    dfs()
                    sol.pop()
        dfs()
        return res
            
        

