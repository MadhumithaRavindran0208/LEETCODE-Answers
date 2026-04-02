class Solution(object):
    def average(self, salary):
        salary.remove(max(salary))
        salary.remove(min(salary))
        return float(sum(salary))/len(salary)
class Solution(object):
    def average(self, salary):
        return float(sum(salary)-max(salary)-min(salary))/(len(salary)-2)
        