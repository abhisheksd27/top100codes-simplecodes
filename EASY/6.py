#Greatest of two numbers: 
#Method 1: Using if-else Statements
'''num1, num2 = 20 , 30
if num1>num2:
  print(num1)
else:
  print(num2)'''
#Method 2: Using Ternary Operator
'''num1, num2 = 20 , 30
print((num1 if num1>num2 else num2))'''
#Method 3: Using inbuilt max() Function
num1, num2 = 20, 30
print(max(num1,num2))