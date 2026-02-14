class Solution(object):
    def longestCommonPrefix(self, strs):
        prefix = ""
        for characters in zip(*strs):
            if len(set(characters)) == 1:
                prefix += characters[0]
            else:
                break
        return prefix