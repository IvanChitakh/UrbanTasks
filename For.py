numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
primes = []
not_primes = []
number = 2
flag = True

for item in numbers:
    if item == 1:
        continue
    while number < item:
        if item % number == 0:
            not_primes.append(item)
            flag = False
            break
        number += 1
    if flag == True:
        primes.append(item)
    number = 2
    flag = True
         
print(f'Primes: {primes}')
print(f'Not Primes: {not_primes}')