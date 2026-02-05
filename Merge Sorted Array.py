class Solution(object):
    def merge(self, nums1, m, nums2, n):
        '''a=[]
        for i in range (m+n):
            if i<m:
                a.append(nums1[i])
            elif m-1<i and i<m+n+1:
                a.append(nums2[i-m])
        return sorted(a)'''
        nums1[m:] = nums2[:n]
        nums1.sort()