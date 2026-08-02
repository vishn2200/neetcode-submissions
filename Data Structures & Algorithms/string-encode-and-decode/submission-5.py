class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == []:
            return "None"
        else:
            s=strs[0]
        for i in strs[1:]:
            s = s + "!@#$%^&*()!@#$%^&*()" + i
        return s


    def decode(self, s: str) -> List[str]:
        if s == "None":
            return []
        else:   
            res = s.split("!@#$%^&*()!@#$%^&*()")
            return res