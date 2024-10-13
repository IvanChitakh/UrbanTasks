data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]
Int_count = 0
Str_count = ''


def de_Sum_Of_Data_Structure(x):
    global Int_count, Str_count
    for i in x:
        if type(i) == list:
            de_Sum_Of_Data_Structure(i)
        if type(i) == dict:
            for j in i:
                l = i.get(j)
                if type(l) == int:
                    Int_count += int(l)
                if type(l) == str:
                    Str_count += l
            de_Sum_Of_Data_Structure(i)
        if type(i) == set:
            de_Sum_Of_Data_Structure(i)
        if type(i) == tuple:
            de_Sum_Of_Data_Structure(i)
        if type(i) == int:
            Int_count += int(i)
        if type(i) == str:
            Str_count += i
            
    return Int_count + len(Str_count)


print(de_Sum_Of_Data_Structure(data_structure))