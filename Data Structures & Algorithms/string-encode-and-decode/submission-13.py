class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == []:
            return ""
        s = ""
        for i in strs:
            s = s + str(len(i)) + "*" + i
        return s


    def decode(self, s: str) -> List[str]:
        if s == "":
            return []
        else:   
            
            res = []
            while s!="":
                
                length = 0
                temp = 0
                for i in range(len(s)):
                    if s[i] == "*":
                        temp = len(s[:i])
                        length = int(s[:i])
                        break
                # print(temp)
                # print(length, s)
                res.append(s[temp + 1:length+temp+1])
                # print(res)
                # print(length + 2 == len(s))
                if length + temp + 1 == len(s):
                    # print("ahbvoahebvoaeuh")
                    break
                else:
                    s = s[length+temp+1:]
            # print(res)
            return res
