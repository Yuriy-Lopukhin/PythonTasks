#Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
#Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
#Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов 
#второго множества. Затем пользователь вводит сами элементы множеств.

n1 = int(input('Введите количество элементов первого множества: '))
n2 = int(input('Введите количество элементов второго множества: '))
A = set()
B = set()
С = set()
for i in range(n1):
    A.add(int(input('Введите элемент первого множества: ')))
for j in range(n2):
    B.add(int(input('Введите элемент второго множества: ')))
C = A & B
#C.sort()
print(C)
