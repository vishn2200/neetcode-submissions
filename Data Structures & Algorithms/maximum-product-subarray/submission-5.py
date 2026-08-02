class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        i = 0
        cur = 1
        temp = []
        max_prod = int()
        while i<len(nums):
            print(temp)
            if nums[i]>0:
                # print(i)
                if cur!=0:
                    cur*=nums[i]
                else:
                    cur = nums[i]
                max_prod = max(max_prod,cur)
                i+=1
            else:
                # print(temp)
                temp.append((cur,i))
                print(temp)
                if len(temp)%2==0:
                    cur = temp[0][0]*nums[temp[0][1]]*temp[1][0]*nums[temp[1][1]]
                    temp = []
                    max_prod = max(max_prod,cur)
                    i+=1
                else:
                    cur = 1
                    i+=1
        
        return max_prod        
        
        