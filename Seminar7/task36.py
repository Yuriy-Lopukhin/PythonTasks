# Задача 36: Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6),
# которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и
# столбца. Аргументы num_rows и num_columns указывают число строк и столбцов таблицы,
# которые должны быть распечатаны. Нумерация строк и столбцов идет с единицы (подумайте,
# почему не с нуля). Примечание: бинарной операцией называется любая операция, у которой
# ровно два аргумента, как, например, у операции умножения.


def print_operation_table(operation,rows,columns):   
    for i in range(1,rows+1):
        print()
        for j in range(1,columns+1):
            print(operation(i,j), end="  ")

user_rows = int(input("Введите число строк: "))
user_сolumns = int(input("Введите число столбцов: "))


print_operation_table(lambda x, y: x * y, user_rows, user_сolumns)