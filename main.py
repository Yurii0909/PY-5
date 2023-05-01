'''Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.
Пример:
A = 3; B = 5 -> 243 (3⁵)
A = 2; B = 3 -> 8
'''
a = int(input("Введите число "))
b = int(input("Введите степень числа(целое неотрицательно число) "))


def func(a, b):
    if b == 0:
        return 1

    return a * func(a, b - 1)


print(func(a, b))

'''
 Дана строка ( возможно, пустая), состоящая из букв A-Z
 AAAABBBCCXYZDDDDEEEFFFAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBB
 Нужно написать функцию RLE, которая на выходе даст строку вида: A4B3C2XYZD4E3F3A6B28
 И сгенерирует ошибку, если на вход пришла невалидная строка.
 Пояснения:Если символ встречается 1 раз, он остается без изменений;
 Если символ повторяется более 1 раза, к нему добавляется количество повторений.

'''
def rle(input_str: str) -> str:
    if not input_str.isalpha():
        return "невалидная строка"
    temp = input_str[0]
    temp_count = 1
    t = []
    for i in range(1, len(input_str)):
        if temp == input_str[i]:
            temp_count += 1
        else:
            t.append((temp, temp_count))
            temp = input_str[i]
            temp_count = 1
    t.append((temp, temp_count))
    rez_str = ""
    for elem in t:
        if elem[1] > 1:
            rez_str += elem[0]
            rez_str += str(elem[1])
        else:
            rez_str += elem[0]
    return rez_str


print(rle('AAAABBBCCXYZDDDDEEEFFFAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBB'))
print(rle('AAAABBBCCXYZDDDDEEEFFFAAAAAABBBBB5286BBBBBBBBBBBBBBBBBBB'))
print(rle(''))


input_list = ["eat", "tea", "tan", "ate", "nat", "bat"]


def group_word(input_l):
    temp_dict = {frozenset(input_l[0]): [input_l[0]]}
    for i in range(1, len(input_l)):
        key = frozenset(input_l[i])
        if key in temp_dict.keys():
            temp_dict[key].append(input_l[i])
        else:
            temp_dict[key] = [input_l[i]]
    return list(temp_dict.values())


print(group_word(input_list))