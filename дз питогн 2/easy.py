# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

# Подсказка: воспользоваться методом .format()

fruits = ["Яблоко", "Апельсин", "Вишня", "Клубника"]
for i, fruit in enumerate(fruits):
    print(f'{i+1}.{fruit:>9}')



# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.

list1 = ["январь", "февраль","март","апрель", "май", "август"]
list2 = ["май", "июнь", "июль", "август"]

for i in list2:
    if i in list1:
        list1.remove(i)
print(list1)
print(list2)
# 1 из 2 без повсторяющихся.(просто для себя)
print("var2")
list1 = {"январь", "февраль","март","апрель", "май", "август"}
list2 = {"май", "июнь", "июль", "август"}
print(list1 | list2)


# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list2 = []
listnew = len(list1)
for i in range(listnew):
    if list1[i] % 2 == 0:
        list2.append(list1[i]/4)
else:
    list2.append(list1[i] * 2)
print(list2)

