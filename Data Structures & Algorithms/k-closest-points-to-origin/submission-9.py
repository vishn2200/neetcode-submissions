class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        d = {}
        for i in points:
            if tuple(i) not in d:
                d[tuple(i)] = math.sqrt(i[0]**2+i[1]**2)
        temp = list(d.values())
        heapq.heapify(temp)
        print(temp)
        res = []
        for _ in range(k):
            val = heapq.heappop(temp)
            res.append([list(key) for key,value in d.items() if value == val])
        print(res)
        if len(res)>1:
            temp = res[0]
            for i in range(1,len(res)):
                if res[i][0] not in temp:
                    temp.append(res[i][0])
            
            return temp
        else: 
            return res[0]


        