class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        def min_i(a,b):
            if a is None:
                return b
            elif b is None:
                return a
            elif a is None and b is None:
                return amount
            else:
                return min(a,b)
                
        dp = {}
        dp[0] = 0
        for i in range(1,amount+1):
            for coin in coins:
                sub = i-coin
                if sub <0:
                    continue
                if dp.get(sub) is None:
                    dp[i] = min_i(None,dp.get(i))
                else:
                    dp[i] = min_i(dp.get(sub)+1,dp.get(i))
        if amount not in dp or dp[amount] is None:
            return -1
        else:
            return dp[amount]