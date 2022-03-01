
numbers = [0, 1]
i = len(numbers) - 1

index = int(input("vilket fibbonaccital vill du ha?"))
output = 0 if index  == 1 else numbers[i]

while (len(numbers) < index):
    numbers.append(numbers[i]+numbers[i-1])
    i+=1
    output = numbers[i]

print(output)