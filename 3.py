"""3. Сформувати функцію для обчислення індексу максимального елемента масиву
n*n, де 1<=n<=5.
Муха Ігор Євгенійович  122-Г"""

import timeit
import numpy as np  # імпорт NumPy
import random  # імпорт Random

while True:
    x = int(input('Введіть розмірність масиву від 1 до 5: '))  # розмірність масиву
    if x > 5 or x < 0:
        print('Ведіть розмірність від 1 до 5')
        break
    else:
        Z = np.zeros((x, x), dtype=int)
    for i in range(len(Z)):  # проходження по списку
        for j in range(len(Z)):  # проходження по елементам списку
            Z[i, j] = random.randint(-5, 10)
    print(Z)


    def elem_rec(array, I=0, J=0, i=0, j=0):  # рекурсія
        if J == len(array[I]):
            I += 1
            J = 0
        if I == len(array):
            return i, j
        if array[I][J] > array[i][j]:
            i = I
            j = J
        J += 1
        return elem_rec(array, I, J, i, j)


    print('Максимальний елемент з індексом(за рекурсивним рішенням): ', elem_rec(Z))
    time1 = timeit.timeit(number=10000)  # таймер 1
    print('рішення за допомогою рекурсії: ', time1)


    def max_element(f):  # рішення за допомогою ітерації
        max_elem = f[0][0]
        for i in range(len(f)):  # проходження по списку
            for j in range(len(f[i])):
                if f[i][j] > max_elem:
                    max_elem = f[i][j]
        list_index = [(i, j) for i in range(len(f)) for j in range(len(f[i])) if
                      f[i][j] == max_elem]  # Знаходження індексу максимального рядка
        line, column = list_index[0]
        return line, column


    print('Максимальний елемент 3 індексом(за ітераційним рішенням): ', max_element(Z))
    time2 = timeit.timeit(number=10000)  # таймер 1
    print('рішення за допомогою ітерації: ', time2)

'''Для даної задачі вирішення за допомогою рекурсії кращий вибір. Перебір елементів через цикл (ітераційно)
працює повільніше і тому рекурсія для цієї задачі підходить більше через швидкість, читабельність, простоту написання коду і потребу
у рекурсії'''
