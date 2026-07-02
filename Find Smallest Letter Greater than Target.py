class Solution(object):
    def nextGreatestLetter(self, letters, target):
        check=""
        res=""
        if max(letters)<=target:return letters[0]
        else:
            while min(letters)<=target:
                letters.remove(min(letters))
        return min(letters)
class Solution(object):
    def nextGreatestLetter(self, letters, target):
        for i in letters:
            if i>target:return i
        return letters[0]
        