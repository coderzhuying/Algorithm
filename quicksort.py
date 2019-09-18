import random


def partition(array, i, j):
    target = array[i]
    while i < j:
        while i < j and target <= arr[j]:
            j -= 1
        arr[i], arr[j] = arr[j], arr[i]
    
        while i < j and target >= arr[i]:
          i += 1
        arr[i], arr[j] = arr[j], arr[i]
        
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
