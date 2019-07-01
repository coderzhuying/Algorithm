def numPairsDivisibleBy(time):
    needs = [0] * 60
    res = 0
    for i in time:
        if i % 60 == 0:
            res += needs[0]
        else:
            res += needs[60 - (i % 60)]
        needs[i % 60] += 1
        print(res)
    return res


if __name__ == "__main__":
    time = [30,20,150,100,40]
    print(numPairsDivisibleBy(time))
