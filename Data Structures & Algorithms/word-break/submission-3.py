class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        sol = []
        temp = ""
        br = -1
        ex = -1
        for i in range(len(s)):
            # print(sol,br)
            temp+=s[i]
            if temp[br+1:i+1] in wordDict or temp[ex+1:i+1] in wordDict:
                sol.append((temp,i))
                ex = br
                br = i
        if br!=len(s)-1:
            return False
        else:
            return True
        
                