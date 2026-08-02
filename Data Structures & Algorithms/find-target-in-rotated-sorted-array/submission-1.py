class Solution:
    def search(self, nums: List[int], target: int) -> int:
        f = 0
        l = len(nums) -1
        mid = (f+l)//2
        while f<=l:
            if nums[mid] == target:
                
                return mid
            elif target > nums[mid] and nums[f] < nums[l]:
                f = mid + 1
                mid = (f+l)//2
            elif target > nums[mid] and nums[f] > nums[l]:
                l = mid -1
                mid = (f+l)//2
            elif target < nums[mid] and nums[f] < nums[l]:
                l = mid -1
                mid = (f+l)//2
            else:
                f = mid +1 
                mid = (f+l)//2
        return -1