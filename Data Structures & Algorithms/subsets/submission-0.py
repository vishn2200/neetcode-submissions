class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        sol = []
        temp = []
        def backtrack(i):
            nonlocal sol
            nonlocal temp
            if i == len(nums):
                sol.append(temp[:])
                return
            backtrack(i+1)
            temp.append(nums[i])
            backtrack(i+1)
            temp.pop()
        backtrack(0)
        return sol
            