def fibbo(input):
    numbers = [0, 1]
    i = len(numbers) - 1
    output = 0 if input == 1 else numbers[i]
    
    
    while (len(numbers) < input):
        numbers.append(numbers[i]+numbers[i-1])
        i += 1
        output = numbers[i]
    return(output)

n = int(input("vilket är ditt n?"))

for i in range(2,n):
    output = fibbo(i+1)/fibbo(i)
    print(output)