#Positive or Negative number:
#bruteforce
'''n = int(input("enter a  numbne rto find out wether the number is posituive or negative"))
if n<0:
    print("negative number")
elif n>0:
    print("Positive number")
else:
    print("Zero")
'''
#using functions

'''def negorpos(n):
    if n<0:
        print("negative number")
    elif n>0:
        print("Positive number")
    else:
        print("Zero")
n = int(input("enter a  numbne rto find out wether the number is posituive or negative"))
negorpos(n)'''

#Using ternory 
num =15
print("Positive" if num>=0 else "Negative")