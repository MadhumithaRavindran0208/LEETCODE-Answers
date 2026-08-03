class Solution(object):
    def uniqueMorseRepresentations(self, words):
        code=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        result=[]
        for i in words:
            a=""
            for j in i:
                a+=code[ord(j)-ord("a")]
            result.append(a)
        return len(set(result))
        