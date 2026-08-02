class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0:
            return 0
        elif n==1:
            return 1
        elif n == 2:
            return 2
        one,two = 1,2
        for i in range(2,n):
            # print(one,two)
            one,two = two,one+two
        return two