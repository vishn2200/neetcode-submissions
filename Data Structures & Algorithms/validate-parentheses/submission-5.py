class Solution:
    def isValid(self, s: str) -> bool:
        d = {"(":")","{":"}","[":"]"}
        stack = []
        top = -1
        for i in s:
            if i in d.keys():
                stack.append(i)
                top+=1
            elif top>=0:
                if i == d[stack[top]]:
                    top-=1
                    stack.pop()
                else:
                    return False
            else:
                return False
        if top==-1:
            return True
        else:
            return False
        