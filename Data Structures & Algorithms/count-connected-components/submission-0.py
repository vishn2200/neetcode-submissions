class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        ans = 0
        visited = set()
        d = defaultdict(list)
        for a,b in edges:
            d[a].append(b)
            d[b].append(a)
        
        def dfs(i):
            visited.add(i)
            for j in d[i]:
                if j not in visited:
                    dfs(j)
            return
        for i in range(n):
            if i not in visited:
                ans +=1
                dfs(i)
        return ans