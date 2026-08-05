class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        d=set(nums)
        res = 0
        for i in nums:
            
            if i-1 not in d:
                temp = 1
                if i+1 not in d:
                    if temp > res:
                        res = temp
                else:
                    cur = i
                    while cur+1 in d:
                        temp+=1
                        if temp > res:
                            res = temp
                        cur = cur+1
        return res
