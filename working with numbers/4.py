#binary to decimal conversion

#To convert a binary number to decimal we need to perform a multiplication 
# operation on each digit of a binary number from right to left with powers of 2 starting from 0 and add each result to get the decimal number of it.


num=10
binary_val=num
decimal_val=0
base=1

while num>0:
    rem=num%10
    decimal_val+=rem*base
    num =num//10
    base = base *2
    
print(decimal_val)