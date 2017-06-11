from math import sqrt, ceil

def isPrime(n): #проверка на простоту числа
    if n % 2 == 0:
        return n == 2
    d = 3
    for i in range(d, ceil(sqrt(n)) + 1, 2):
        if (n %  d == 0):
            return False
    return True

def factorized(n): #складывание простых множителей в массив
   ans = []
   d = 2
   nsqr = ceil(sqrt(n)) + 1
   while d <= nsqr:
       if n % d == 0:
           ans.append(d)
           n //= d
       else:
           d += 1
   if n > 1:
       ans.append(n)
   return ans