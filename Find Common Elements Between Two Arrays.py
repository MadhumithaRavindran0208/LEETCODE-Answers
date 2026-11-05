class Solution(object):
    def findIntersectionValues(self, nums1, nums2):
        a=0
        for i in nums1:
            if i in nums2:a+=1
        b=0
        for i in nums2:
            if i in nums1:b+=1
        return [a,b]
class Solution(object):
    def findIntersectionValues(self, nums1, nums2):
        a=0
        s1=set(nums1)
        s2=set(nums2)
        for i in nums1:
            if i in s2:a+=1
        b=0
        for i in nums2:
            if i in s1:b+=1
        return [a,b]
        