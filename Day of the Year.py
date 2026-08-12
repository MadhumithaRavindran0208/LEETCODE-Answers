class Solution(object):
    def dayOfYear(self, date):
        year=int(date[0:4])
        month=int(date[5:7])
        day=int(date[8:10])
        days_in_month=[31,28,31,30,31,30,31,31,30,31,30,31]
        if (year%4==0 and year%100!=0)or(year%400==0):
            days_in_month[1]=29
        return sum(days_in_month[:month-1])+day
        