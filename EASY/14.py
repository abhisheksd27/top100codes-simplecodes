'''num = 371
num1 = num
sum1 = 0
leng = len(str(num1))

def arm(num1,leng, sum1):
    if num1 == 0:
        return sum1
    for i in range(leng):
        d = int(num1 % 10)
        sum1 = sum1 + pow(d, leng)
        num1 = int(num1 / 10)  # Update num1 by dividing it by 10
    return sum1

if arm(num1,leng, sum1) == num:
    print("Armstrong number")
else:
    print("Not an Armstrong Number")'''




number = 371
num = number
sum =0
length = len(str(num))
def checkArmstrong(num,length,sum):
  if num==0:
    return sum
  sum+=pow(int(num%10),length)
  return checkArmstrong(num/10,length,sum)

if checkArmstrong(num,length,sum)==number:
  print('Armstrong')
else:
  print("Not Armstrong")