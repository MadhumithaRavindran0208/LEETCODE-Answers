class Solution(object):
    def findDifference(self, nums1, nums2):
        num1=[]
        num2=[]
        nums1=set(nums1)
        nums2=set(nums2)
        for i in nums1:
            if i not in nums2:num1.append(i)
        for i in nums2:
            if i not in nums1:num2.append(i)
        return [num1,num2]