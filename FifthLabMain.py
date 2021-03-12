from FifthLabMergeSort import *
from FifthLabArrays import *
import timeit
import time


if __name__ == "__main__":
    print("1 - Ввести массив вручную\n"
          "2 - Сгенерировать случайный массив\n"
          "3 - Сгенерировать убывающий массив")
    action = input()

    array = []
    if action == "1":
        print("Введите массив через пробел")
        array = list(map(int, input().split()))
    elif action == "2":
        print("Введите размер массива")
        length = int(input())
        array = list(getRandomArray(length))
    elif action == "3":
        print("Введите размер массива")
        length = int(input())
        array = list(getDecreasingArray(length))
    else:
        print("Ошибка!")
        exit(-1)

    print("\nДля вывода значений стоит ограничение в 100 элементов!")
    print("Изначальный массив:")
    print(array[:100])

    # Сортировка слиянием
    start = timeit.default_timer()
    sortedArray = mergeSort(array)
    # time.sleep(12)
    end = timeit.default_timer()
    print("\nОтсортированный массив сортировкой слиянием:")
    print(sortedArray[:100])
    print("Время в секундах: " + '{:0.10f}'.format(end - start))

    # Сортировка python
    start = timeit.default_timer()
    sortedArray = sorted(array)
    end = timeit.default_timer()
    print("\nОтсортированный массив стандартной сортировкой:")
    print(sortedArray[:100])
    print("Время в секундах: " + '{:0.10f}'.format(end - start))
