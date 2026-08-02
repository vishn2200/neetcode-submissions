class KthLargest:
    import heapq
    
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        
    
    def add(self, val: int) -> int:
        self.nums.append(val)
        x = heapq.nlargest(self.k,self.nums)
        print(x)
        return x[-1]
