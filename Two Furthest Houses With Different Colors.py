class Solution(object):
    def maxDistance(self, colors):
        result=0
        n = len(colors)
        for i in range(n - 1, -1, -1):
            if colors[i] != colors[0]:
                result = max(result, i)
                break
        for i in range(n):
            if colors[i] != colors[n - 1]:
                result = max(result, (n - 1) - i)
                break
        return result
        