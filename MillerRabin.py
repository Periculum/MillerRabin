from random import randrange

def isPrime(n):
    # Variables
    exponent = n - 1
    s = 0

    # keep dividing the exponent by two until the result is odd
    while exponent % 2 == 0:
        # Example for n = 41: 40, 20, 10; Stop: exponent = 5
        exponent //= 2
        s += 1

    # generate random number and check the smallest exponent = 5      
    a = randrange(2, n - 1)   
    x = pow(a, exponent, n)
    if x == 1 or x == n - 1:
        return True

    # test the remaining numbers
    while s > 1:
        x = pow(x, 2, n)
        if x == 1:
            return False
        if x == n - 1:
            return True
        s -= 1
        exponent *= 2
    return False

def main():
    print(isPrime(561)) # smallest Carmichael-Number (you can put any uneven Number here)


if __name__ == '__main__':
    main() 
