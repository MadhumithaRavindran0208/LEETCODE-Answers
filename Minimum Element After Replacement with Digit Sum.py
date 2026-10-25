class Solution(object):
    def minElement(self, nums):
        for i in range(len(nums)):
            if nums[i]<10:continue
            else:
                a=0
                for j in str(nums[i]):
                    a+=int(j)
                nums[i]=a
        return min(nums)
class Solution(object):
    def minElement(self, nums):
        final=nums[0]
        for i in nums:
            a=0
            while i>0:
                a+=i%10
                i//=10
            final=min(final,a)
        return final
                    