#Prime number within a given rang
#Method 1: Using inner loop Range as [2, number-1].
'''low, high = 2, 10
primes = []

for i in range(low, high + 1):
    flag = 0

    if i < 2:
        continue
    if i == 2:
        primes.append(2)
        continue

    for x in range(2, i):
        if i % x == 0:
            flag = 1
            break

    if flag == 0:
        primes.append(i)
        
print(primes)'''
#Method 2: Using inner loop Range as [2, number/2].
'''low, high = 2, 10
primes = [2]

for num in range(low, high + 1):
    flag = 0
    if num < 2:
        flag = 1
        
    if num % 2 == 0:
        continue
    iter = 2

    while iter < int(num / 2):
        if num % iter == 0:
            flag = 1
            break
        iter += 1

    if flag == 0:
        primes.append(num)

print(primes)'''
#Method 3: Using inner loop Range as [2, sqrt(number)].
'''low, high = 2, 10
primes = [2, 3]

for num in range(low, high + 1):
    flag = 0
    
    if num < 2:
        flag = 1
        
    if num % 2 == 0:
        continue
        
    if num % 3 == 0:
        continue
        
    iter = 2
    while iter < int(pow(num, 0.5)):
        if num % iter == 0:
            flag = 1
            break
        iter += 1
        
    if flag == 0:
        primes.append(num)

print(primes)'''
#Method 4: Using inner loop Range as [3, sqrt(number), 2].
low, high = 2, 10
primes = [2, 3]

for num in range(low, high + 1):
    flag = 0
    if num < 2:
        flag = 1

    if num % 2 == 0:
        continue
        
    if num % 3 == 0:
        continue

    iter = 3

    while iter < int(pow(num, 0.5)):
        if num % iter == 0:
            flag = 1
            break
        iter += 2

    if flag == 0:
        primes.append(num)

print(primes)