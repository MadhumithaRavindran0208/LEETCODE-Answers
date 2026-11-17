class Solution(object):
    def pivotArray(self, nums, pivot):
        less=[]
        equal=[]
        great=[]
        for i in nums:
            if i==pivot:equal.append(i)
            elif i<pivot:less.append(i)
            else:great.append(i)
        return less+equal+great