def summa(num):
    return num + num

listik = [1,4,5, 6, 6, 7, 7, 8, 8, 9, 9, 9, 9, 9, 9, 9]

def my_map(func, iterable):
    my_list = []
    for item in iterable:
        res = func(item)
        my_list.append(res)
    return print(my_list)

my_map(summa, listik)

print('map is updated')