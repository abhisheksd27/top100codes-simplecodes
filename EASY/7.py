#Greatest of the Three numbers:
#Method 1: Using if-else Statements

'''
num1, num2, num3 = 10 , 30 , 20
max = 0
if num1 >= num2 and num1 >= num3:
  print(num1)
elif num2 >= num1 and num2 >= num3:
  print(num2)
else:
  print(num3)'''
#Method 2: Using Nested if-else Statements

'''num1, num2, num3 = 10 , 350 , 550
max = 0
if num1 >= num2:
    if num1 >= num3:
        print(num1)
elif num2 >= num1:
    if num2 >= num3:
        print(num2)
    else :
        print(num3)'''
#Method 3: Using Ternary Operator
num1, num2, num3 = 10 , 30 , 20
max = num1 if num1>num2 else num2
max = num3 if num3>max else max
print(max)