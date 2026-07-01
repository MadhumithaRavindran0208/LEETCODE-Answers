class Solution(object):
    def checkPossibility(self, nums):
        def is_sorted(arr):
            return all(arr[i] <= arr[i+1] for i in range(len(arr)-1))

        for i in range(len(nums) - 1):
            if nums[i] > nums[i+1]:
                return (is_sorted(nums[:i] + nums[i+1:]) or is_sorted(nums[:i+1] + nums[i+2:]))
        return True
        