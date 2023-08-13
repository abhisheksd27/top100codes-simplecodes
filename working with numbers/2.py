
#highest common factor
#LCM of two numbers is the smallest common multiple or a positive integer which is divisible completely by both the numbers.


a=12
b=14
arr=[]
for i in range(min(a,b),(a*b)+1):
    if(i%a==0 and i%b==0):
        arr.append(i)
print(min(arr))