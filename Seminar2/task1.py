# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты
# вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть.
# 5 -> 1 0 1 1 0
# 2

M = int(input('Введите общее количество монет: '))
o,r = 0,0
for i in range(M):
    x = int(input('Орел(1) или решка(0)?: '))
    if x == 1:
        o += 1
    else:
        r += 1
if o < r:
    print(f'Переверните {o} монет(ы) на решку, их меньше всего')
elif o == r:
    print(f'Количество орлов и решек одинаково: по {o} штук(и)')
else:
    print((f'Переверните {r} монет(ы) на орла, их меньше всего'))
