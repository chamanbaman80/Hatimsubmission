a=int(input("Enter a number: "))


def factorial(n):

    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
result=factorial(5)
print("The factorial of ", 5 , " is ", result)


