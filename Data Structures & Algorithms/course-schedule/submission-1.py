class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        d = {}
        # visited = set()
        for i in prerequisites:
            if i[0] not in d:
                d[i[0]] = [i[1]]
            else:
                d[i[0]].append(i[1])            
            
        def dfs(key,visited):
            nonlocal d
            visited.add(key)
            if key not in d:
                return True
            for i in d[key]:
                if i in visited:
                    return False
                return dfs(i,visited)
            # return True

        for key in d:
            visited = set()
            if not dfs(key,visited):
                return False
            else:
                continue
        return True
        
        