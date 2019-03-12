#!/usr/bin/python

def main():
    '''
    If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

    Find the sum of all the multiples of 3 or 5 below 1000.
    '''

    print multiples3n5(1000)

def multiples3n5(number)
    sum = 0
    for i in range(0, number):
        if i % 3 == 0 or i % 5 == 0:
            sum += i

    # prints out 233168 which is the correct answer
    return sum

if __name__ == "__main__":
    main()