class Solution(object):
    def squareIsWhite(self, coordinates):
        test1=["a","c","e","g","1","3","5","7"]
        test2=["b","d","f","h","2","4","6","8"]
        if coordinates[0] in test1:
            return coordinates[1] not in test1 
        elif coordinates[0] in test2:
            return coordinates[1] not in test2
        