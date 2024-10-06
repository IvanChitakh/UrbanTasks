# The needed solution
def cipher(stone1):
    dividers = []
    right_Cipher = ''
    for i in range(3, stone1 + 1):
        if stone1 % i == 0:
            dividers.append(i)
    iter = 1
    while iter <= int(stone1 / 2):
        for divider in dividers:
            if divider / iter <= 2:
                continue
            right_Cipher += str(iter) + str(divider - iter)
        iter += 1

    return right_Cipher


stone1 = int(input())
print(cipher(stone1))
