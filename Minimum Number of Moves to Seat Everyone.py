class Solution(object):
    def minMovesToSeat(self, seats, students):
        seats=sorted(seats)
        students=sorted(students)
        result=0
        for i in range(len(seats)):
            result+=abs(students[i]-seats[i])
        return result
