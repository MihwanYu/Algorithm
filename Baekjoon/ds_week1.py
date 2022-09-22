import math

n = 0
k = 1
s = 0

while n != 100:
    n = n+1
    if k==math.log(n, 3):
        k = k+1
        s = s+n
        print('interim s: ',s)
    else:
        pass

print('result: ',s)