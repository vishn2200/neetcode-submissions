class Solution:
    def search(self, nums: List[int], target: int) -> int:
        f = 0
        l = len(nums) - 1
        mid = (l+f)//2
        while f<=l:
            if target > nums[mid]:
                f = mid + 1
                mid = (l+f)//2
            elif target < nums[mid]:
                l = mid -1
                mid = (l+f)//2
            else:
                return mid
        return -1

        