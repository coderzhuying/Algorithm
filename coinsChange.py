def coinChange(n):
    """
    硬币找零问题，成倍数用贪心
    :param n:
    :return:
    """
    res = 0
    coins = [64, 16, 4, 1]
    n = 1024 - n
    for coin in coins:
        res += n // coin
        n %= coin
    return res

print(coinChange(201))