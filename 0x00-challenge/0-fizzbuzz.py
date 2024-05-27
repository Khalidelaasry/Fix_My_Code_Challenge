#!/usr/bin/python3
""" FizzBuzz
"""
import sys


def fizzbuzz(limit):
    """
    FizzBuzz function prints numbers from 1 to limit separated by a space.

    - For multiples of three print "Fizz" instead of the number and for
      multiples of five print "Buzz".
    - For numbers which are multiples of both three and five print "FizzBuzz".
    """
    if limit < 1:
        return

    result_list = []
    for num in range(1, limit + 1):
        if (num % 3) == 0 and (num % 5) == 0:
            result_list.append("FizzBuzz")
        elif (num % 3) == 0:
            result_list.append("Fizz")
        elif (num % 5) == 0:
            result_list.append("Buzz")
        else:
            result_list.append(str(num))
    print(" ".join(result_list))


if __name__ == '__main__':
    if len(sys.argv) <= 1:
        print("Missing number")
        print("Usage: ./0-fizzbuzz.py <number>")
        print("Example: ./0-fizzbuzz.py 89")
        sys.exit(1)

    input_number = int(sys.argv[1])
    fizzbuzz(input_number)
