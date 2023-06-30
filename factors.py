#!/usr/bin/python3
import sys

def factorize(n):
    factors = []
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

def main():
    if len(sys.argv) != 2:
        print("Usage: factors <file>")
        return
    
    filename = sys.argv[1]
    with open(filename, 'r') as file:
        numbers = file.read().splitlines()
    
    for number in numbers:
        n = int(number)
        factors = factorize(n)
        factors_str = "*".join(str(f) for f in factors)
        print(f"{n}={factors_str}")

if __name__ == '__main__':
    main()
