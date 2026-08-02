class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
         
        states = [0]*n
        d = defaultdict(list)
        for a,b in edges:
            if a == b:
                return False
            d[a].append(b)
            d[b].append(a)
        def dfs(i,cur):
            
            if states[i] == 1:
                return False
            elif states[i] ==2:
                return True
            states[i] = 1

            for j in d[i]:
                if j != cur:  
                    if not dfs(j,i):
                        return False
            states[i] = 2
            return True
        # for i in range(n):
            
        #     if not dfs(i,i):
        #         return False
        if not dfs(0,0):
            return False
        if 0 in states:
            return False
        return True
