class Solution:
    from itertools import permutations,combinations
    def numDecodings(self, s: str) -> int:
        if s[0] == "0":
            return 0
        else:
            dp = {len(s):1}
            for i in range(len(s)-1,-1,-1):
                if i+1 == len(s):
                    if s[i] == "0":
                        dp[i] = 0
                    else:
                        dp[i] = dp[i+1]
                else:
                    if s[i]=="0":
                        dp[i] = 0
                    elif int(s[i]) > 2:
                        dp[i] = dp[i+1]
                    elif int(s[i]) == 2 and int(s[i+1])>6:
                        dp[i] = dp[i+1]
                    
                    else:
                        dp[i] = dp[i+1]+dp[i+2]
            return dp[0]

