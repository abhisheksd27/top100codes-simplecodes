#Reverse of a number : 

'''num=123
rev=0
while num!=0:
    i=int(num%10)
    rev=(rev*10)+i
    num=num//10
print(rev)'''

#using recursion

num=123
rev=0
def reve(num,rev):
    if num==0:
        return rev
    i=int(num%10)
    rev=(rev*10)+i
    
    return reve(int(num//10),rev)

print(reve(num,rev))