# This function returns True when a number is prime
def is_prime(n):
    from math import sqrt
    for i in range(2,int(sqrt(n))+1):
        if n%i==0:
            return False
    return True
