def generator(n):
    """ Returns  a list of primes < n taken from https://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n"""
    sieve = [True] * n
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)//(2*i)+1)
    return [2] + [i for i in range(3,n,2) if sieve[i]]

def factorization(x):
    factors = []
    z = 1
    factor = getFactor(x)
    while True:
       
        if x/z == 1:
            break
        factors.append(factor(x/z))              
        z = z * factors[-1]        
        
        
    return factors

def getFactor(x):
   
    primes = generator(int(x**0.5))
    def n(y):
        limit = y**0.5
        for i in primes:
            if i < limit:
                if y % i == 0:            
                    return i
            else:
                break
        return int(y)
    return n
