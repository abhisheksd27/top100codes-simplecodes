#Sum of N natural numbers:
#Using for Loop
'''number,sum = 6,0
for i in range(number+1):
  sum+=i
print(sum)'''

#Using formula
'''number = 6
sum = int((number * (number + 1))/2)
print(sum)'''

#using recursion

def recursum(number):
  if number == 0:
    return number
  return number + recursum(number-1)
number, sum = 6,0
print(recursum(number))