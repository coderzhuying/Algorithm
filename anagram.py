"""
有效的字母异位词
"""


def isAnagram3(s, t):
    """
    排序
    :param s:
    :param t:
    :return:True或False
    """
    return sorted(s) == sorted(t)


def isAnagram2(s, t):
    """
    使用字典统计
    :param s:
    :param t:
    :return:
    """
    dic1, dic2 = {}, {}
    for item in s:
        dic1[item] = dic1.get(item, 0) + 1
    for item in t:
        dic2[item] = dic2.get(item, 0) + 1

    return dic1 == dic2


def isAnagram(s, t):
    """
    自己手动构造哈希函数
    :param s:
    :param t:
    :return:
    """
    ls1, ls2 = [0]*26, [0]*26
    for item in s:
        ls1[ord(item)-ord('a')] += 1
    for item in t:
        ls2[ord(item)-ord('a')] += 1

    return ls1 == ls2


if __name__ == "__main__":
    s = "wearehappy"
    t = "wehappyare"
    tp = "wehappyere"

    print(isAnagram3(s, t))
    print(isAnagram2(s, t))
    print(isAnagram(s, t))