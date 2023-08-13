#Even or Odd number
#Using Brute Force
'''num = int(input("Enter a Number:")) 
if num % 2 == 0: 
  print("Given number is Even") 
else: 
  print("Given number is Odd")'''

#Using Ternary Operator

'''num = 17
print("Even") if num%2 == 0 else print("Odd")'''

#Using Bitwise Operator

def isEven(num):
  return not num&1

if __name__ == "__main__":
  num = 13
  if isEven(num):
    print('Even')
  else:
    print('Odd')