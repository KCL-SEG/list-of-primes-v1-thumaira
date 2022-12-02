"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    list = []
    i= 2
    while len(list)< number_of_primes:
        prime = True
        number+=1
        for i in range (2, number//2+1):
            if (number % i)==0:
                prime = False
                break
        if prime:
            list.append(number)
        return list
