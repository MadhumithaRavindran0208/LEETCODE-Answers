class Solution(object):
    def arithmeticTriplets(self, nums, diff):
        c=0
        l=len(nums)
        for i in range(l-2):
            for j in range(i+1,l-1):
                if nums[j]-nums[i]==diff:
                    for k in range(j+1,l):
                        if nums[k]-nums[j]==diff:
                            c+=1
                            break
        return c
class Solution(object):
    def arithmeticTriplets(self, nums, diff):
        s=set(nums)
        l=len(nums)
        c=0
        for i in s:
            if i+diff in s and i+diff*2 in s:c+=1
        return c
        