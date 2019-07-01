class Insert:

    def insertSort(self, array):
        """
        直接插入排序
        :param array: 需要排序的数组
        :return: 排好序的数组
        """
        length = len(array)
        for i in range(1, length):
            if array[i] < array[i-1]:
                j = i - 1
                t = array[i]
                while array[j] > t and j >= 0:
                    array[j+1] = array[j]
                    j = j - 1
                array[j+1] = t

        return array

    def biInsertSort(self, array):
        """
        折半插入排序
        :param array: 待排序的数组
        :return: 已经排好序的数组
        """
        length = len(array)
        for i in range(1, length):
            if array[i-1] > array[i]:
                t = array[i]
                high = i - 1
                low = 0
                while low <= high:
                    mid = int((high+low)/2)
                    if array[mid] > t:
                        high = mid - 1
                    else:
                        low = low + 1
                j = i - 1
                while j >= low:
                    array[j+1] = array[j]
                    j = j -1

                array[j+1] = t

        return array


if __name__ == '__main__':
    insert = Insert()
    print(insert.biInsertSort([1,4,2,7,3,9,0]))