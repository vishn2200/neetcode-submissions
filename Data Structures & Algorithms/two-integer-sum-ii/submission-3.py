class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        mid = target//2 if target%2==0 else target//2 + 1
        l = 0
        r = len(numbers) - 1
        while numbers[l] <= mid and numbers[r] >= mid:
            if numbers[l] + numbers[r] > target:
                r -= 1
            elif numbers[l] + numbers[r] < target:
                l += 1
            else:
                return [l+1, r+1]
