#Sum of First N Natural numbers: 
#Using for Loop
'''num = 5
sum = 0
for i in range(num+1):
  sum+=i
print(sum)'''


#Using Formula for the Sum of Nth Term
'''
num = 5
print(int(num*(num+1)/2))'''

#Using Recursion

def getSum(num):
  if num == 1:
    return 1
  return num + getSum(num-1)

num = 5
print(getSum(num))