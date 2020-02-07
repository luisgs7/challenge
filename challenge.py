k = [7, 6, 4, 3, 1]
t = len(k)
r, a = 0, 0

for x in k:
    a += 1
    b = a
    while(b < t):
        value = (k[b] - x)
        if(value >= r):
            r = value
        b += 1

print(r)





    