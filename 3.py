import math as m
index=int(input("vilket fibbonaccital vill du ha?"))
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
print(output)