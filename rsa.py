#!/usr/bin/python3

import random
import math

def modular_pow(base, exponent, modulus):
    result = 1
    while (exponent > 0):
        if (exponent % 2 != 0):
            result = (result * base) % modulus
        exponent = int(exponent / 2)
        base = (base * base) % modulus
    return result


def prime_divisor(n):
    if (n == 1):
        return n
    if (n % 2 == 0):
        return 2

    x = (random.randint(0, 2) % (n - 2))
    y = x
    c = (random.randint(0, 1) % (n - 1))

    d = 1
    while (d == 1):
        x = (modular_pow(x, 2, n) + c + n) % n

        y = (modular_pow(y, 2, n) + c + n) % n
        y = (modular_pow(y, 2, n) + c + n) % n

        d = math.gcd(abs(x - y), n)

        if (d == n):
            return prime_divisor(n)
    return d


def print_factors(number):
    div = prime_divisor(number)
    num = int(number / div)
    if div >= num:
        print("{:d}={:d}*{:d}".format(number, div, num))
    else:
        print("{:d}={:d}*{:d}".format(number, num, div))
        


def main():
    from sys import argv, exit, stderr

    if len(argv) != 2:
        stderr.write("Usage: ./factors <file>\n")
        exit()

    try:
        f = open(argv[1], "r")
    except FileNotFoundError:
        stderr.write("Could not find file {}, not exist\n".format(argv[1]))
    else:
        while (True):
            line = f.readline()
            if (not line):
                break
            line = int(line)
            print_factors(line)
    
    f.close()


main()
