import math as m


def fibbo(index):
    numbers = [0, 1]
    i = len(numbers) - 1
    output = 0
    if index == 1:
        output = 0
    elif index == 2:
        output = 1
    while (len(numbers) < index):
        numbers.append(numbers[i]+numbers[i-1])
        i+=1
        output = numbers[i]
    return(output)

n = int(input("vilket är ditt n?"))

for i in range(2,n):
    output = fibbo(i+1)/fibbo(i)
    print(output)