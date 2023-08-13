#Prime number:
#Method 1: Simple iterative solution

'''num = 15
flag = 0
for i in range(2,num):
  if num%i==0:
    flag = 1
    break
if flag == 1:
  print('Not Prime')
else:
  print("Prime")'''
#Method 2: Optimization by break condition

'''num = 15
flag = 0
if num<2:
  flag = 1
else:
  for i in range(2,num):
    if num%i==0:
      flag = 1
      break

if flag == 1:
  print('Not Prime')
else:
  print("Prime")'''
#Method 3: Optimization by n/2 iterations
'''num = 15
flag = 0
if num<2:
  flag = 1
else:
  for i in range(2,int((num/2)+1)):
    if num%i==0:
      flag = 1
      break

if flag == 1:
  print('Not Prime')
else:
  print("Prime")'''
#Method 4: Optimization by √n
'''num = 7
flag = 0
if num<2:
  flag = 1
else:
  for i in range(2,int(pow(num,0.5)+1)):
    if num%i==0:
      flag = 1
      break

if flag == 1:
  print('Not Prime')
else:
  print("Prime")'''
#Method 5: Optimization by skipping even iteration
'''num = 15
flag = 0
if num<2:
  flag = 1
elif num == 2:
  flag = 0
else:
  for i in range(3,int(pow(num,0.5)+1),2):
    if num%i==0:
      flag = 1
      break

if flag == 1:
  print('Not Prime')
else:
  print("Prime")'''
#Method 6: Basic Recursion technique
num = 15
def checkPrime(num,iter=2):
  if num == iter:
    return True
  if num%iter==0:
    return False
  if num<2:
    return False
  return checkPrime(num,iter+1)
if checkPrime(num)==True:
  print("Prime")
else:
  print("Not Prime")