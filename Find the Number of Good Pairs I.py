class Solution(object):
    def numberOfPairs(self, nums1, nums2, k):
        c=0
        for i in nums1:
            for j in nums2:
                if i%(j*k)==0:c+=1
        return c
class Solution(object):
    def numberOfPairs(self, nums1, nums2, k):
        c=0
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i]%(nums2[j]*k)==0:c+=1
        return c
        