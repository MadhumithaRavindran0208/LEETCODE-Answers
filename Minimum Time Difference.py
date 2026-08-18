class Solution(object):
    def findMinDifference(self, timePoints):
        result = []
        for i in range(len(timePoints)):
            result.append(int(timePoints[i][:2]) * 60 + int(timePoints[i][3:]))
        result.sort()
        returning = float("inf")
        for i in range(len(result) - 1):
            returning = min(result[i+1] - result[i], returning)
        wrap = 1440 - result[-1] + result[0]
        returning = min(returning, wrap)
        return returning