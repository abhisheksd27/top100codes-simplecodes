#sum of digits of a number
'''num=123
num1=str(num)
sum=0
for i in num1:
    sum+=int(i)
print(sum)'''

#or 
'''num=123
sum=0
while num!=0:
    n=int(num%10)
    sum+=n
    num=num/10
print(sum)'''

#Using Recursion


num=1234
sum=0
def sumof(num,sum):
    if num == 0:
        return sum
    i = int(num%10)
    sum += i
    num=num/10
    return sumof(num,sum)

print(sumof(num,sum))

