# First, mine solution
def cipher(stone1):
    dividers = []
    right_Cipher = ''
    for i in range(3, stone1 + 1):
        if stone1 % i == 0:
            dividers.append(i)
    print(dividers)
    for i in dividers:
        num1, num2 = 1, i - 1
        while i / num1 > 2.0:
            if i == num1 + num2:
                print(str(num1), str(num2))
                right_Cipher += str(num1) + str(num2)
            num1 += 1
            num2 -= 1

    return right_Cipher


stone1 = int(input())
print(cipher(stone1))