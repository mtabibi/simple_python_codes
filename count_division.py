
# Define number of divisions of n
def how_many_division(n):
    from math import sqrt
    count=0
    for i in range(1,int(sqrt(n))+1): # use sqrt to run program faster
        if n%i==0:
            if n/i==i: # n is a squared number
                count+=1
            else:       # n/i=j ==> i , j both are devisions
                count+=2
    return count
