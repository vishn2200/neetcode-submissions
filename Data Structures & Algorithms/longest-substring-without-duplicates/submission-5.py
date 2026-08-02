class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if len(s) == 0:
            return 0
        elif len(s) == 1:
            return 1
        max_len = 0
        i = 0
        j = 1
        dup = {s[i]}
        while j<len(s) and i < len(s):
            # print(dup)
            if s[j] not in dup:
                dup.add(s[j])
                max_len = max(max_len, len(s[i:j+1]))
                j+=1
            else:
                dup.remove(s[i])
                i+=1
        return max_len
