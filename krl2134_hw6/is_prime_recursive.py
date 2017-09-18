'''
Name: Kevin Li
UNI: krl2134
Date: 4 November 2016

is_prime_recursive is a recursive function that returns whether input n is
prime
'''

def is_prime_recursive(n, d):
    #n is the number to check for primality and d is the divisor to check. 
    while d >= 2:
        if n % d == 0:
            return False
        else:
            return is_prime_recursive(n, d-1)
    else:
        return True
