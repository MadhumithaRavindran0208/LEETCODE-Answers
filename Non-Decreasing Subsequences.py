class Solution(object):
    def findSubsequences(self, nums):
        final = set()
        n = len(nums)
        def build(start, current):
            if len(current) >= 2:
                final.add(tuple(current))
            for i in range(start, n):
                if not current or nums[i] >= current[-1]:
                    build(i + 1, current + (nums[i],))
        build(0, ())
        return list(final)
        