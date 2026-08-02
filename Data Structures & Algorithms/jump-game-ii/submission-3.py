class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n== 1:
            return 0
        jumps = 0
        target = n-1
        def calc(target):
            nonlocal jumps
            if target == 0:
                return jumps
            for i in range(target):
                if nums[i] + i >= target:
                    jumps+=1
                    target = i
                    return calc(target)
        calc(n-1)
        return jumps