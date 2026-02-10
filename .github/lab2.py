#Factorial
def factorial(n):
    if n == 0 or n == 1:   
        return 1
    else:
        return n * factorial(n - 1)  

num = int(input("Enter a number: "))
print("Factorial of", num, "is", factorial(num))

#Word count
sentence = input("Enter a sentence: ")
words = sentence.split()
print("Number of words:", len(words))

#fibonacci
def fibonacci(n):
    if n <= 0:
        return "Invalid input"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

num = int(input("Enter the position (n): "))
print(f"Fibonacci number at position {num} is {fibonacci(num)}")
