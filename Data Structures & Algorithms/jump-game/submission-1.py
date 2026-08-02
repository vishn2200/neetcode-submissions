class Solution:
    def canJump(self, nums: List[int]) -> bool:
        target = len(nums)-1
        for i in range(target-1,-1,-1):
            if target - i <= nums[i]:
                target = i

        if target == 0:
            return True
        else:
            return False