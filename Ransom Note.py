class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        c=set(ransomNote)
        for i in c:
            if ransomNote.count(i)>magazine.count(i):return False
        else:return True
        