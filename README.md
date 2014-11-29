## DOUBLY PRIME NUMBERS README

**Background**: 

This program generates N doubly prime numbers. A doubly prime number is defined as 
a prime number that also has  it's constituting digits  being prime.


*Example*:
  
    > 5 is prime and it's made up of the number 5 which is prime. Therefore, it's doubly prime
    
    > 13 is prime and it's made up of the numbers 1 which is prime and 3 which is also prime. Therefore, it's doubly prime.

*Counter example*: 

    > 19 is prime.  1 is prime but 9 isn't since it's divisible by 3. Therefore, 19 is not doubly prime. 


*What is the smallest prime number?*

Original definitions of prime numbers included 1. However, recent definitions states that prime numbers begin at 2. 
A look at [Wikipedia definition of prime numbers] (http://en.wikipedia.org/wiki/Prime_number) attests to this. Also, 
[a paper published in the Journal of Integer Sequences] (https://cs.uwaterloo.ca/journals/JIS/VOL15/Caldwell1/cald5.pdf) 
tries to explain why the smallest prime number is not 1. 

However, instructions for this assignment adheres to the original definition of prime numbers which includes 1.
 Therefore, the program treats 1 as a valid prime number.
 
 
**Some observations**
 
 * Changing the first prime number from 1 to 2 has a huge effect on the total number of doubly prime numbers this implementation can generate and the time it takes to generate them.
 
 
**How to run**
 1. Ensure you have git installed. Refer to [this] (http://git-scm.com/book/en/v2/Getting-Started-Installing-Git) for git installation instructions. 
 2. Clone this repo by running the following command from within the directory into which you want the clone created:
 
    > git clone https://github.com/cnokello/doubly-primed.git
    
3. If not yet installed, install Python 3 by following the instructions:

    * [Linux installation](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python).
    * [Windows installation](https://docs.python.org/3/using/windows.html#installing-python)
    * [MacOS installation](https://docs.python.org/3/using/mac.html#getting-and-installing-macpython)

4. Ensure you add PYTHON_HOME to your PATH variable.

5. Then, from within the directory into which you cloned the code in 2 above, run: 

    > python src/intervw/DoublyPrimeNumberGenerator.py
    
    Sample output for N = 100:
        
    > List(1, 2, 3, 5, 7, 11, 13, 17, 23, 31, 37, 53, 71, 73, 113, 127, 131, 137, 151, 157, 173, 211, 223, 227, 233, 251, 257, 271, 277, 311, 313, 317, 331, 337, 353, 373, 521, 523, 551, 557, 571, 577, 727, 733, 751, 757, 773, 1117, 1121, 1123, 1151, 1153, 1171, 1213, 1217, 1223, 1231, 1237, 1273, 1277, 1321, 1327, 1373, 1511, 1523, 1531, 1537, 1553, 1571, 1577, 1711, 1721, 1723, 1733, 1753, 1777, 2111, 2113, 2117, 2131, 2137, 2153, 2173, 2213, 2221, 2237, 2251, 2273, 2311, 2333, 2351, 2357, 2371, 2377, 2521, 2531, 2537, 2551, 2557, 2711)
     