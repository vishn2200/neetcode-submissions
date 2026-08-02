class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = dict()
        for i in nums:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        res = [item[0] for item in sorted(d.items(), key=lambda item: item[1])]
        res = res[::-1]
        return res[0:k]


         