class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums = sorted(nums)
        # print(nums)
        for i in range(len(nums) - 2):
            l = i+1
            r = len(nums) - 1
            temp = -(nums[i])
            while l < r:
                # print(i, l, r)
                if nums[l] + nums[r] < temp:
                    l += 1
                elif nums[l] + nums[r] > temp:
                    r -= 1
                else:
                    if [nums[i], nums[l], nums[r]] not in res:
                        res.append([nums[i], nums[l], nums[r]])
                    # print("HIT")
                    l += 1
                    
        return res