from statistics import median
class MedianFinder:
    
    def __init__(self):
        self.heap = []

    def addNum(self, num: int) -> None:
        # heapq.heapify(self.heap)
        heapq.heappush(self.heap,num)
        return

    def findMedian(self) -> float:
        # temp = self.heap
        # sort = []
        # for i in temp:
        #     sort.append(heapq.heappop(temp))
        return median(self.heap) 
        