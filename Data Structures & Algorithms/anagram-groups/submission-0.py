class Solution:

    def isAnagram(self, s1: str, s2: str) -> bool:
        s1 = "".join(sorted(s1))
        s2 = "".join(sorted(s2))
        if s1 == s2:
            return True
        else:
            return False


    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        for i in strs:
            flag = 0
            if len(res) == 0:
                res.append([i])
                flag = 1
                continue
            
            for j in range(len(res)):
                # print(i, res[j][0])
                if self.isAnagram(i, res[j][0]):
                    res[j].append(i)
                    flag = 1
                    break
            if flag == 0:
                res.append([i])
        return res
            