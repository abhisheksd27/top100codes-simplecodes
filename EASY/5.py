#Sum of numbers in a given range: 
# Using Brute Force
'''num1, num2 = 3, 6
sum = 0
for i in range(num1,num2+1):
  sum+=i
print(sum)'''
#Using the Formula
'''
num1, num2 = 3, 6
sum = int((num2*(num2+1)/2) - (num1*(num1+1)/2) + num1)
print(sum)'''
#Using Recursion

def recursum(sum,num1,num2):
  if num1 > num2:
    return sum
  return num1 + recursum(sum,num1+1,num2)

num1, num2 = 3, 6
sum = 0
print(recursum(sum,num1,num2))