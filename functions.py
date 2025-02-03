#header file for all functions

import math
import random
import sys

random.seed()

'''
2/3/2025

@author Carlos & Kade
'''

def testPrime(p): #fermat's little algorithm
    k = 500 #number of times to test the prime
    
    if p <= 3:
        return True
    if p % 2 == 0:
        return False
    
    for x in range(k):
        a = random.randint(2, p-2)
        if (pow(a, p-1, p) != 1):
            return False
    return True
        
        

def genPrime():
    prime = random.randrange(2, sys.maxsize) #generate big integer based on max size of system
    
    isPrime = False
    
    while not isPrime: #loop until prime is found
        prime = random.randrange(2, sys.maxsize)
        isPrime = testPrime(prime)
    
    return prime

def EuclidGCD(a, b): #euclid's gcd
    if b == 0:
        return a
    else:
        return EuclidGCD(b, a%b)
    
def extendedEuclidGCD(a=1, b=1): #euclid's extended gcd
    
    if b==0:
        
        return(1, 0, a)
    
    (x, y, d) = extendedEuclidGCD(b, a%b)
    
    return y, x-a//b*y, d

def genKey():
    p = genPrime()
    q = genPrime()
    n = p*q
    phi = (p-1) * (q-1)
    
    e = random.randrange(2, phi) #generate a random integer from 2 - phi
    
    while True: #test if e is a relative prime of phi
        if (EuclidGCD(e, phi) == 1):
            break
        else:
            e = random.randrange(2, phi) #generate random e until e is relatively prime
    
    x = extendedEuclidGCD(e, phi) #generate extended euclid gcd to determine d
    d = x[0]%phi
    
    return e, d, n
    
    
