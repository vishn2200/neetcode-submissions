class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s)==1:
            return s[0]
        max_l = 1
        ans = ""
        
        for k in range(len(s)):
            i,j = k,k
            
            while i>-1 and j<len(s) and s[i]==s[j]:
                if j-i+1>max_l:
                    ans = s[i:j+1]
                    max_l = j-i+1
                if i == 0 and j != len(s)-1:
                    j+=1
                elif j == len(s)-1 and i!=0:
                    i-=1
                else:
                
                    i-=1
                    j+=1
    
            i = k
            j = k+1
            while i>-1 and j<len(s) and s[i]==s[j]:
                if j-i+1 > max_l:
                    max_l = j-i+1
                    ans = s[i:j+1]
                if i == 0 and j != len(s)-1:
                    j+=1
                elif j == len(s)-1 and i!=0:
                    i-=1
                else:
                
                    i-=1
                    j+=1
        return ans if len(ans)>1 else s[0]
