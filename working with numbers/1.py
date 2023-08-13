#highest common factor


a=360
b=600
num = []
for i in range(1,max(a,b)):
    if(a%i==0 and b%i==0):
        num.append(i)
print(max(num))