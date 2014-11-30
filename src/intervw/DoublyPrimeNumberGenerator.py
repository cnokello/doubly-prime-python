'''
Created on Nov 29, 2014

@author: nelson.okello
'''
from lib2to3.fixer_util import String
import math
import sys, getopt

class DoublyPrimeNumberGenerator(object):
    
    
    '''
    This class generates doubly prime numbers of length numPrimes
    '''

    def __init__(self, numPrimes):
        '''
        Constructor
        '''
        self.N = numPrimes
        
    
        
    def generateDoublyPrimes(self):
        """Returns a list of doubly prime numbers with length numPrimes"""
        
        def isPrime(n: int):
            """ Returns True if n is a doubly prime number. False otherwise"""
            if n < 1: return False 
            elif (n == 1 or n == 2): return True
            elif (n > 2 and n % 2 == 0): return False
            
            return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))
        
        def isAllPrime(nString: String):
            """ Returns True if all the numeric characters in the string are prime numbers
                False otherwise."""
            for c in nString:
                if  not isPrime(int(c)):
                    return False
            
            return True
    
        primes = [1, 2]
        numPrimes = 2  # cache length of primes generated so far
        nextNum = 3  # next integers to test for primality

        while numPrimes < self.N:
            if isPrime(nextNum) and isAllPrime(str(nextNum)):
                primes.append(nextNum)
                numPrimes += 1
            nextNum += 2  # # Skip testing even numbers

        return primes

   
# # Run the doubly prime number generator
# # Retrieve passed arguments
if(len(sys.argv) == 1):    
    N = 100 
elif(len(sys.argv) == 2):
    N = int(sys.argv[1])
else: print("Invalid arguments passed. Format: python src/intervw/DoublyPrimeNumberGenerator.py <N>")
    
# # Now, run the generator
dpnGen = DoublyPrimeNumberGenerator(N)
primes = list(dpnGen.generateDoublyPrimes())
print(primes)
print("No. of double prime numbers generated: " + str(len(primes)))
