class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sol = []
        for i in range(len(nums)-2):
            for j in range(i+1,len(nums) - 1):
                for k in range(j+1, len(nums)):
                    if nums[i]+nums[j]+nums[k] == 0:
                        flag = 0
                        for x in sol:
                            if sorted([nums[i],nums[j],nums[k]]) == sorted(x):
                                flag = 1
                                break
                        if flag == 0:
                            sol.append([nums[i],nums[j],nums[k]])

        return sol