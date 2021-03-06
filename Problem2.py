#Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

#1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

#By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
import math
def sumEvenFibonacci(n):
    golden = 0.5 + ((5**0.5) / 2)
    """Finding the number closest to n"""
    nearestPlace = round(math.log(n*(5**0.5),golden))
    """Every third term is divisible by two so our limit is the coeficient between nearesPlace and 3 """
    limit = nearestPlace // 3
    x = 0
    """We calculate the fibonacci number in the 3, 6, 9 and so on places using Binet's Formula"""
    for i in range(limit+1):
        x += round(((golden**(i*3)) - ((1 - golden)**(i*3)))/(5**0.5))
    return x
