"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    list = []
    for number in range(number_of_primes):
        if number>1:
            for i in range (2, number):
                if (number % i)==0:
                    break
            else:
                list.append(number)
    print(list)

primes(10)
