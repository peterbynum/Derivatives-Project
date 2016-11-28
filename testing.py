def drange(start, stop, step): # Defines new range function to allow for noninteger increments
    r = start
    while r < stop:
        yield r
        r += step
f = input('function: ')
startinterval = int(input("start of interval: "))
stopinterval = int(input("stop of interval: "))
poi = []
nderiv = lambda m,n,h: (m-n)/(2*h)
for x in drange(startinterval, stopinterval, abs((stopinterval-startinterval)/10000)): # 10000 iterations for every interval
    increment = abs((stopinterval-startinterval)/10000)
    h = abs((stopinterval-startinterval)/100000000) # no matter how small the interval the h values adjust
    fpplus = nderiv(eval(f.replace("x","(x+2*h)")), eval(f), h)
    fpminus = nderiv(eval(f), eval(f.replace("x","(x-2*h)")), h)
    left = nderiv(fpplus, fpminus, h)
    x += increment
    fpplus = nderiv(eval(f.replace("x","(x+2*h)")), eval(f), h)
    fpminus = nderiv(eval(f), eval(f.replace("x","(x-2*h)")), h)
    right = nderiv(fpplus, fpminus, h)
    intervalaverage = (2*x-increment)/2
    if right == 0: # redifferentiates the righthand side with a larger increment if right previously is zero
        x += increment
        fpplus = nderiv(eval(f.replace("x","(x+2*h)")), eval(f), h)
        fpminus = nderiv(eval(f), eval(f.replace("x","(x-2*h)")), h)
        right = nderiv(fpplus, fpminus, h)
        intervalaverage = (x-increment)
    if (left < 0 and right > 0) or (left > 0 and right < 0):
        poi.append(intervalaverage)
poi = [round(i, 3) for i in poi]
print(poi)
