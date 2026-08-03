class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pref = []
        for i in range(len(nums)):
            if i > 0:
                pref.append(temp1)
                temp1 = temp1*nums[i]
            else:
                pref.append(0)
                temp1 = nums[0]
        suff =[0 for i in range(len(nums))]
        for i in range(len(nums) -1, -1, -1):
            if i != len(nums) - 1:
                suff[i] = temp2
                temp2 = temp2 * nums[i]
                if i == 1:
                    suff[0] = temp2
                    break
            else:
                temp2 = nums[i]
                continue
        res = []
        print(pref)
        print(suff)
        for i in range(len(nums)):
            if i == 0:
                res.append(suff[i])
            elif i == len(nums) -1:
                res.append(pref[i])
            else:
                res.append(pref[i]*suff[i])
        return res

    
        