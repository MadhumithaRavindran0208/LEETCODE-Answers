class Solution(object):
    def numSpecialEquivGroups(self, words):
        signatures = set()
        for word in words:
            even = sorted(word[0::2])  
            odd  = sorted(word[1::2]) 
            signatures.add((tuple(even), tuple(odd)))
        return len(signatures)