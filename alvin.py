n = int(input("Enter a positive number:"))

factorial = 1
while n > 0:
    factorial *= n 
    n -= 1
print("The Factorial is:", factorial)