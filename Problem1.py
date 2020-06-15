def findMultiples(x,y,z):
    limitx = (z-1) // x
    limity = (z-1) // y
    limitw = (z-1) // (x*y)
    sumx = (x * ((limitx*(limitx+1))/2))
    sumy = (y *((limity*(limity+1))/2))
    sumw = (x*y*((limitw*(limitw+1))/2))
    sumation = int(sumx + sumy - sumw) 
    return sumation
