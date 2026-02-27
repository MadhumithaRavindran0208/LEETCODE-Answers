class Solution(object):
    def sortColors(self, nums):
        c0=0
        c1=0
        c2=0
        for i in nums[::]:
            if i==0:
                c0+=1
            if i==1:
                c1+=1
            if i==2:
                c2+=1
        nums[:c0]=[0]*c0
        nums[c0:c1+c0]=[1]*c1
        nums[c1+c0:]=[2]*c2
        return nums
class Solution(object):
    def sortColors(self, nums):
        nums.sort()
        return nums