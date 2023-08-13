#Factorial of a number
def fact(num):
    if num==0:
        return 1
    
    return num*fact(num-1)

num=6

print(fact(num))