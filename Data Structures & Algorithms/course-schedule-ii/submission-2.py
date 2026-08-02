class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        d = defaultdict(list)
        for a,b in prerequisites:
            d[a].append(b)
        # visited = set()
        # flag = 0
        res = []
        states = [0]*numCourses
        def dfs(i):
            if states[i] == 1:
                return False
            if states[i] == 2:
                return True
            states[i] = 1
            for j in d[i]:
                if not dfs(j):
                    return False
            res.append(i)
            states[i] = 2
            return True
            
        for i in range(numCourses):
            if not dfs(i):
                return []
        return res