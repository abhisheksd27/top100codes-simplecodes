#Harshad number 
n = 21
p=n
sum1=0
while(n>0):
    sum1+=n%10
    n=n//10
if(p%sum1==0):
    print("Harshad number")
else:
    print("Not harshad number")