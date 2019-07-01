def heapify_big(array, n, i):
    """
    将子树构建成大顶堆
    :param array:数组
    :param n:数组元素个数
    :param i:子树的root
    :return:
    """
    if i >= n:
        return
    c1 = 2 * i + 1
    c2 = 2 * i + 2
    max = i
    if c1 < n and array[c1] > array[max]:
        max = c1

    if c2 < n and array[c2] > array[max]:
        max = c2

    if max != i:
        array[max], array[i] = array[i], array[max]
        heapify_big(array, n, max)
    return array


def heapify_small(array, n, i):
    """
    将子树构建成小顶堆
    :param array:数组
    :param n:数组元素个数
    :param i:子树的root
    :return:
    """
    if i >= n:
        return
    c1 = 2 * i + 1
    c2 = 2 * i + 2
    min = i
    if c1 < n and array[c1] < array[min]:
        min = c1

    if c2 < n and array[c2] < array[min]:
        min = c2

    if min != i:
        array[min], array[i] = array[i], array[min]
        heapify_small(array, n, min)
    return array


def build_heap(array, n):
    """
    构建顶堆
    :param array: 无序数组
    :param n: 数组元素个数
    :return: 构建好的顶堆
    """
    last_node = n - 1
    parent_node = int((last_node - 1) / 2)
    i = parent_node
    while i >= 0:
        heapify_big(array, n, i)
        # heapify_small(array, n, i)
        i = i - 1

    return array


def heap_sort(array):
    """
    堆排序
    :param array: 乱序数组
    :return:有序数组
    """
    n = len(array)
    build_heap(array, n)
    i = n - 1
    while i >= 0:
        array[0], array[i] = array[i], array[0]
        heapify_big(array, i, 0)
        # heapify_small(array, i, 0)
        i = i - 1

    return array


def top_k(array, k):
    """
    在固定数组取最大的前k个
    思路:构建大顶堆,sort做一半,将最大的前k个放到[-k:]
    :param array:
    :param k:
    :return: array[-k:]
    """
    n = len(array)
    build_heap(array, n)
    i = k - 1
    j = n - 1
    while i >= 0:
        array[0], array[j] = array[j], array[0]
        heapify_big(array, j, 0)
        print(array)
        i = i - 1
        j = j - 1
    return array[-k:]


def add(array, k, n):
    """
    对top_k返回的数组中如果继续加入新的元素,求top_k
    思路:在固定长度为k的数组里维护小顶堆
    :param array:固定长度为k的数组
    :param k:
    :param n:新的元素
    :return:array
    """
    if n > array[0]:
        n, array[0] = array[0], n
        return heapify_small(array, k, 0)
    else:
        return array


if __name__ == "__main__":
    k = 4
    top = top_k([3, 7, 6, 1, 3, 0, 3, 5], k)
    print(top)
    for i in range(100):
        print(add(top, k, i))

