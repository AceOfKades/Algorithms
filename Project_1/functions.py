#header file for all functions

import random
import sys

random.seed()

'''
2/3/2025

@author: Carlos & Kade & Carson
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

def stringToASCII(string):
    asciiMessage = "127" # garbage character of length 3 at the start, to be removed at decryption
    for x in string:
        char = str(ord(x))
        if len(char) < 3:
            if len(char) == 1:
                char = "00" + char
            elif len(char) == 2:
                char = "0" + char
        asciiMessage += char
        
    return int(asciiMessage)

def ASCIItoString(integer):
    string = ""
    temp = str(integer)
    
    #remove garbage character at start of string
    temp = temp[3:]
    
    for x in range(len(temp)//3):
        x = temp[:3]
        string += chr(int(x))
        temp = temp[3:]
    
    return string
    
def fastExpo_rec (c,d,n):
    if d == 0:
        return 1 
    t = fastExpo_rec(c,d//2, n)
    t = (t*t)%n
    
    if d%2 == 0:
        return t
    else:
        return (c*t) % n  
  
def chunkMessage(message, chunkSize):
    return [message[i:i+chunkSize] for i in range(0, len(message), chunkSize)]

def padChunk(chunk, chunkSize):
    return chunk.zfill(chunkSize)

def calcMaxChunk(n):
    max_size = len(str(n))-1
    if max_size%3 != 0:
        max_size -= max_size%3
    return max_size
    
def EncryptMessage(message, e, n):
    ascii_message = stringToASCII(message)
    
    max_chunk_size = calcMaxChunk(n)
    
    chunkHold = chunkMessage(str(ascii_message), max_chunk_size)
    paddedChunks = [padChunk(chunk, max_chunk_size) for chunk in chunkHold]
    
    encryptedChunks = []
    for chunk in paddedChunks:
        encryptedChunk = fastExpo_rec(int(chunk), e, n)
        encryptedChunks.append(str(encryptedChunk))
    
    return " ".join(encryptedChunks)
    
def DecryptMessage(encryptedMessage, d, n):
    encryptedChunks = encryptedMessage.split(" ")
    max_chunk_size = calcMaxChunk(n)
    
    decryptedChunks = []
    for chunk in encryptedChunks:
        chunkHold = fastExpo_rec(int(chunk), d, n)
        decryptedChunks.append(str(chunkHold).zfill(max_chunk_size))
    
    decryptedChunks[-1] = decryptedChunks[-1].lstrip("0")
    
    difference = len(decryptedChunks[-1])%3
    if (difference != 0):
        difference = 3-difference
        decryptedChunks[-1] = decryptedChunks[-1].zfill(difference+len(decryptedChunks[-1]))
        
    
    ascii_message = "".join(decryptedChunks)
    return ASCIItoString(ascii_message)
 
def authenticateSignature(message, signature, e, n):
    decryptSignature = DecryptMessage(signature, e, n)
    
    return (message == decryptSignature)
    
    
    
