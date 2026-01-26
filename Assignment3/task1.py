#task1: factorial of number

num=int(input("Enter a number: "))
def factorial(num):
    factorial=1
    while num>1:
        factorial=factorial * num
        num-=1
    return factorial

print(f"Factorial of {num} is: {factorial(num)}")
