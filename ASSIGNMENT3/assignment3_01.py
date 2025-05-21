num=int(input("Enter a number: "))

def fact(num):
    if num<2:
        return 1
    return num * fact(num-1)

print("Factorial of",num,"is:",fact(num))