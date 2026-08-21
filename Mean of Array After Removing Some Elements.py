class Solution(object):
    def trimMean(self, arr):
        arr.sort()
        n=len(arr)
        trim=int(n*0.05)
        trimmed=arr[trim:n-trim]
        return float(sum(trimmed))/len(trimmed)