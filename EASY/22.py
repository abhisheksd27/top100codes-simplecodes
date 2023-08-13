#Perfect number :
'''n = 28
sum = 0

for i in range(1, n):
    if n % i == 0:
        sum = sum + i

if sum == n:
    print("The number is a Perfect number")
else:
    print("The number is not a Perfect number")'''
    
    
sum_n = 0

def getSumDivisors(num, i):
    global sum_n
    # since, all factors can be found will num/2
    # we will only check in this range
    if i <= num // 2:

        if num % i == 0:
            sum_n = sum_n + i

        i += 1

        # recursively call isPerfect
        getSumDivisors(num, i)

    # returns the sum
    # when i becomes > num/2
    return sum_n


num = 28

if getSumDivisors(num, 1) == num:
    print("The number is a Perfect number")
else:
    print("The number is not a Perfect number")