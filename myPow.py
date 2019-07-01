def mypow(x, n):
    if not n:
        return 1
    if n < 0:
        return 1/mypow(x, -n)
    if n % 2:
        return x * mypow(x, n-1)
    return mypow(x*x, n/2)


def no_re_mypow(x, n):
    if n < 0:
        x = 1/x
        n = -n
    pow = 1
    while n:
        if n % 2:
            pow = pow * x
        x = x * x
        n = int(n/2)

    return pow


if __name__ == "__main__":
    print(no_re_mypow(2, -5))