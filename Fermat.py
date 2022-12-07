# Fermattest
from random import randrange


def isPrime(n):
    a = randrange(2, n)
    return pow(a, n - 1, n) == 1

# this method runs 1000 times the Fermattest and counts the amount of True and False
# it returns a quote where 0 stands for prime, and 1.0 for not prime
# everthing inbetween means there are some false positives (so be careful with the final result)
# Carmichael-Numbers like 561 or 8911 generate usually a lot of false positives
def testQuote(tries, n):
    z = 0
    for i in range(tries):
        if not isPrime(n):
            z += 1
    return z / tries 


def main():
    n = input("Please insert an uneven Number: ")
    print(testQuote(1000, int(n)))


if __name__ == '__main__':
    main()
