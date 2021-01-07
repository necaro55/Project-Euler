#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

#Find the sum of all the multiples of 3 or 5 below 1000.
def findMultiples(x,y,z):
    limitx = (z-1) // x
    limity = (z-1) // y
    limitw = (z-1) // (x*y)
    sumx = (x * ((limitx*(limitx+1))/2))
    sumy = (y *((limity*(limity+1))/2))
    sumw = (x*y*((limitw*(limitw+1))/2))
    sumation = int(sumx + sumy - sumw) 
    return sumation
