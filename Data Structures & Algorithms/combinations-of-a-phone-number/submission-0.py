class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        d = {
            2:"abc",
            3:"def",
            4:"ghi",
            5:"jkl",
            6:"mno",
            7:"pqrs",
            8:"tuv",
            9:"wxyz"
        }
        res = []
        sol = ""
        def backtrack(i):
            nonlocal res
            nonlocal sol
            if i == len(digits):
                res.append(sol[:])
                return
            for j in range(len(d[int(digits[i])])):
                sol+=d[int(digits[i])][j]
                backtrack(i+1)
                sol = sol[:-1]
                # backtrack(i+1)
        backtrack(0)
        return res