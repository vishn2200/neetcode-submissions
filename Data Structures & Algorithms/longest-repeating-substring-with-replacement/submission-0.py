class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if not s:
            return 0
        elif len(s) == 1:
            return 1
        n = len(s)
        max_len = 0
        i = 0
        j = 1
        def possible(s,i,j,k):
            d = {}
            for x in range(i,j+1):
                if s[x] not in d:
                    d[s[x]] = 1
                else:
                    d[s[x]] += 1
            if sum(d.values()) - (max(d.values()) + k) >0:
                return False
            else:
                return True
        while j < n and i < n:
            if possible(s,i,j,k):
                max_len = max(max_len, j-i+1)
                j+=1
            else:
                i += 1
        return max_len
