#!/usr/bin/python

def main():
    '''
    The prime factors of 13195 are 5, 7, 13 and 29.

    What is the largest prime factor of the number 600851475143 ?
    '''

    # prints out 6857 which is the correct answer
    print largestPrimeFactor(600851475143)


def largestPrimeFactor(number):
    i = 2
    factors = []
    while i * i <= number:
        if number % i:
            i += 1
        else:
            number //= i
            factors.append(i)
    if number > 1:
        factors.append(number)

    factors.sort()

    return factors[len(factors)-1]


if __name__ == "__main__":
    main()
