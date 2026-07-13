class Solution(object):
    def topKFrequent(self, nums, k):
        freq = {}
        for n in nums:
            freq[n] = freq.get(n, 0) + 1
        return sorted(freq, key=lambda x: freq[x], reverse=True)[:k]