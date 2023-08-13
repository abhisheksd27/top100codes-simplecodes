#Factor of a number :

num=12
a=[]
if num==0:
    print("enter the valid value ")
else:
    for i in range(2,num):#if we want to include the num itself(num+1)
        if num%i==0:
            a.append(i)
        else:
            continue
    
print(a)
        