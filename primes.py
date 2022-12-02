"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    list = []
    number=1
    i= 2
    while len(list)< number_of_primes:
        number+=1
        for i in range (1, number):
            if (number % i)==0:
                break
            else:
                list.append(number)
        print(list)
primes(20)
