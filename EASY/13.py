#Palindrome number
num=int(121)
pal=0
def palindrome(num,pal):
    if num==0:
        return pal
    i=(num%10)
    pal=(pal*10)+i
    return palindrome((num//10),pal)
revers=palindrome(num,pal)

if num==revers:
    print("Palindrome")
else:
    print("Not a palindrome")