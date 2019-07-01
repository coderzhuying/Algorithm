class Solution:
    def mysqrt(self, x):
        r = x
        while r * r > x:
            r = (r + x / r) / 2
        return r


if __name__ == "__main__":
    n = int(input())
    solution = Solution()
    print(solution.mysqrt(n))