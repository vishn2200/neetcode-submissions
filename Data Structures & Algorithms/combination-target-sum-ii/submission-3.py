class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        sol = []
        def dfs(i,cur_sum):
            if cur_sum == target:
                flag = 0
                for j in res:
                    if sorted(j) == sorted(sol[:]):
                        flag = 1
                        break
                if flag == 0:

                    res.append(sol[:])
                    return
            if cur_sum > target or i == len(candidates):
                return
            sol.append(candidates[i])
            dfs(i+1,sum(sol[:]))
            sol.pop()
            dfs(i+1,sum(sol[:]))
            
        dfs(0,0)
        return res
