class Solution(object):
    def longestSubsequence(self, arr, difference):
        dp = {}
        for num in arr:
            dp[num]=dp.get(num-difference,0)+1
        return max(dp.values())
        