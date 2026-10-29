class Solution(object):
    def asteroidsDestroyed(self, mass, asteroids):
        asteroids.sort()
        for i in asteroids:
            if mass<i:return False
            mass+=i
        return True