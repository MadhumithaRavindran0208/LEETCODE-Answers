class Solution(object):
    def heightChecker(self, heights):
        n=0
        a=zip(sorted(heights),heights)
        for i in a:
            if i[0]!=i[1]:
                n+=1
        return (n)