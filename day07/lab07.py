## Exercise 1
## Write a function using recursion to calculate the greatest common divisor of two numbers

## Helpful link:
## https://www.khanacademy.org/computing/computer-science/cryptography/modarithmetic/a/the-euclidean-algorithm
def gcd(x, y):
    if x==0:
        return y
    elif y==0:
        return x
    else:
        r = x%y
        return gcd(r,y)

gcd(100,50)

## Exercise 2
## Write a function using recursion that returns prime numbers less than 121
def find_primes(me = 121, primes = []):
    if me == 2:
        primes.append(me)
        return primes
    else:
       for i in range(me,-1,-1):
           for j in range(i,-1,-1):
               if i%primes[j]!=0:
                   primes.append(i)
                   return primes
               

def find_primes(me = 121, primes = []):
    for i in range(me,-1,-1):
        for j in range(i,-1,-1):
            if i%primes[j]!=0:
                   primes.append(i)
                   return primes
            else:
                find_primes(me==i)
primes   