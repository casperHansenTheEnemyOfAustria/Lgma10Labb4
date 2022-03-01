import math as m
n=int(input("Hur många triangeltal ska beräknas?")) 
out = 0
for iterator in range(1, n):
    out = out + iterator
    print(out)