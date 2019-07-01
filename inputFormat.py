def manyLines():
    lines = int(input())
    array = []
    i = 0
    while i < lines:
        s = input()
        subarray = s.split(",")
        for n in range(len(subarray)):
            subarray[n] = int(subarray[n])
        array.append(subarray)
        i += 1
    print(array)


def singleLine():
    s = input()
    array = s.split(" ")
    for i in range(len(array)):
        array[i] = int(array[i])

    print(array)


if __name__ == "__main__":
    # manyLines()
    singleLine()
