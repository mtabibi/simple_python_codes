"""This function returns True when a number is prime
this function is faster
because it deletes numbers which their first digit is even or 5
except 2 and 5 themselves"""
def is_prime(n):
    from math import sqrt
    num_str=str(n)
    if n==2 or n==5:
        return True
    if n==1:
        return False
    if num_str[-1] in ['2','5']:
        return False
    for i in range(2,int(sqrt(n))+1):
        if n%i==0:
            return False
    return True
