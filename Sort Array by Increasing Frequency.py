class Solution(object):
    def frequencySort(self, nums):
        d={}
        for i in nums:
            d[i]=d.get(i,0)+1
        nums.sort(key=lambda x: (d[x], -x))
        return nums