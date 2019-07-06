def autoCalibration(s):
    """
    字符串处理，假的自动校验工具
    :param s:
    :return:
    """
    len(s)
    i = -1
    while i < len(s):
        i += 1
        if i + 3 > len(s):
            break
        if s[i] == s[i+1] == s[i+2]:
            s = s[0: i+2] + s[i+3:]
            i -= 1
        if i + 4 > len(s):
            continue
        if s[i] == s[i+1] and s[i+2] == s[i+3]:
            s = s[0:i+3] + s[i+4:]
            i -= 1
    return s


if __name__ == "__main__":
    n = int(input())
    arr = []
    for i in range(n):
        arr.append(input())
    for i in range(n):
        print(autoCalibration(arr[i]))




