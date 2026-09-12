class Solution(object):
    def stableMountains(self, height, threshold):
        result=[]
        for i in range (len(height)-1):
            if height[i]>threshold:result.append(i+1)
        return result