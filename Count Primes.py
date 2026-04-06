class Solution(object):
    def countPrimes(self, n):
        l=[]
        for i in range (2,n):
            no=0
            for j in range (2,i):
                if i%j==0:
                    no+=1
                    break
            if no==0:
                l.append(i)
        return (len(l))
class Solution(object):
    def countPrimes(self, n):
        if n <= 2:
            return 0
        is_prime = [True] * n
        is_prime[0] = is_prime[1] = False  
        for i in range(2, int(n**0.5) + 1):
            if is_prime[i]:
                for j in range(i*i, n, i):
                    is_prime[j] = False
        return sum(is_prime)