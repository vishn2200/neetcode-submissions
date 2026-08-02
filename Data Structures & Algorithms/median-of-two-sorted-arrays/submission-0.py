class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        c = []
        i = 0
        j = 0
        while i<len(nums1) and j < len(nums2):
            if nums1[i]<=nums2[j]:
                c.append(nums1[i])
                i+=1
            else:
                c.append(nums2[j])
                j+=1
        if i!=len(nums1):
            c.extend(nums1[i::])
        else:
            c.extend(nums2[j::])
        # print(c)
        if (len(nums1)+len(nums2))%2==0:
            return (c[(len(nums1)+len(nums2))//2] + c[(len(nums1)+len(nums2))//2 -1])/2
        else:
            return c[(len(nums1)+len(nums2))//2]