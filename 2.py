import math as m
start=int(input("Ditt starttal?")) 
diff=int(input("Differensen mellan två på varandra följande tal"))
length=int(input("hur många tal skall visas i din följd?"))
output = 0
for i in range(0, length):
        output+=start+diff*i
print("summan är " + str(output))
