def mergeSort(array):  # TODO: Передавать массив по ссылке, а не по значению
    if len(array) > 1:
        mid = len(array) // 2
        leftArray = mergeSort(array[:mid])  # Копия левой части рекурсивно сортируется
        rightArray = mergeSort(array[mid:])  # Копия правой части рекурсивно сортируется
        sortedArray = merge(leftArray, rightArray)  # Слияение отсортированных копий изначального массива
    else:
        sortedArray = array  # Возврат ссылки на переданный в функцию массив
    return sortedArray


def merge(leftArray, rightArray):
    sortedArray = []
    lIndex = 0
    rIndex = 0
    while len(sortedArray) != (len(leftArray) + len(rightArray)):
        if lIndex == len(leftArray):  # Если левый массив полностью записан
            sortedArray.append(rightArray[rIndex])
            rIndex += 1
        elif rIndex == len(rightArray):  # Если правый массив полностью записан
            sortedArray.append(leftArray[lIndex])
            lIndex += 1
        else:
            if leftArray[lIndex] <= rightArray[rIndex]:
                sortedArray.append(leftArray[lIndex])
                lIndex += 1
            elif rightArray[rIndex] < leftArray[lIndex]:
                sortedArray.append(rightArray[rIndex])
                rIndex += 1
    return sortedArray
