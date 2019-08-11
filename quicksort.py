import random


def partition(array, i, j):
    target = array[i]
    while i < j:
        while i < j and target > array[i]:
            i += 1
        while i < j and target < array[j]:
            j -= 1
        array[i], array[j] = array[j], array[i]

    return i


def QSort(array, i, j):
    if i < j:
        pivot = partition(array, i, j)

        QSort(array, i, pivot-1)
        QSort(array, pivot+1, j)


def QuickSort(array):
    QSort(array, 0, len(array)-1)


if __name__ == '__main__':
    array = [random.randint(0, 20) for _ in range(5)]
    print(array)
    QuickSort(array)
    print(array)
