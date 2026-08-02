class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        sol = []
        def backtrack(i):
            if i == len(nums):
                flag = 0
                for i in res:
                    if sorted(i) == sorted(sol[:]):
                        flag = 1
                        break
                if flag == 0:
                    res.append(sol[:])
                return
            backtrack(i+1)
            sol.append(nums[i])
            backtrack(i+1)
            sol.pop()
        backtrack(0)
        return res
            