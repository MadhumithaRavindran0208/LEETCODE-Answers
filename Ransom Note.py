class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        c=set(ransomNote)
        for i in c:
            if ransomNote.count(i)>magazine.count(i):return False
        else:return True
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        c=set(ransomNote)
        m={}
        for i in magazine:
            m[i]=m.get(i,0)+1
        r={}
        for i in ransomNote:
            r[i]=r.get(i,0)+1
        for i in c:
            if m.get(i,0)<r[i]:return False
        else:return True
        
