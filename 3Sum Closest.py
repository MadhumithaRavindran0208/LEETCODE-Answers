class Solution(object):
    def threeSumClosest(self, nums, target):
        n=len(nums)
        nums.sort()
        final=sum(nums[:3])
        for i in range(n-2):
            if i>0 and nums[i]==nums[i-1]:continue
            left,right=i+1,n-1
            while left<right:
                s=nums[i]+nums[left]+nums[right]
                if abs(s-target)<abs(final-target):final=s
                if s==target:return s          
                elif s<target:left+=1         
                else:right-=1 
        return final  