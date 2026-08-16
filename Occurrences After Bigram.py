class Solution(object):
    def findOcurrences(self, text, first, second):
        result=[]
        text=text.split(" ")
        for i in range (len(text)-2):
            if text[i]==first and text[i+1]==second:result.append(text[i+2])
            i+=2
        return result