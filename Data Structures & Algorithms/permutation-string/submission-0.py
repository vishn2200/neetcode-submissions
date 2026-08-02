class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1 = len(s1)
        i = 0
        j = n1-1
        d1 = {}
        for y in s1:
            if y not in d1:
                d1[y] = 1
            else:
                d1[y]+=1
        
        def check(s1,s2,i,j,d1):
            d2 = {}
            for x in s2[i:j+1]:
                if x not in d2:
                    d2[x] = 1
                else:
                    d2[x]+=1
            if d1 == d2:
                return True
            else:
                return False
        while j<len(s2):
            if check(s1,s2,i,j,d1):
                return True
            else:
                i+=1
                j+=1
        return False

