# Мог бы сделать код, где можно было бы самому подавать на ввод имя и оценки столько, сколько захочется.

grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students = sorted(students)
done_Dict = []

def class_Dict():
    runner = 0
    for name in students:
        aver_Grade = sum(grades[runner]) / len(grades[runner])
        done_Dict.append(name), done_Dict.append(aver_Grade)
        aver_Grade = 0
        runner += 1
    print(done_Dict)

class_Dict()