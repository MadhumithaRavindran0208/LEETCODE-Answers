class Solution(object):
    def sortPeople(self, names, heights):
        a=zip(heights,names)
        a.sort(reverse=True)
        return [name for heights,name in a]
        