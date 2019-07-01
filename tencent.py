def minDistance(s):
    stack = []
    for i in range(len(s)):
        if not stack:
            stack.append(s[i])
        else:
            if stack[-1] == '0' and s[i] == '1':
                stack.pop()
            elif stack[-1] == '1' and s[i] == '0':
                stack.pop()
            else:
                stack.append(s[i])
    return len(stack)


if __name__ == "__main__":
    count = input()
    s = input()
    print(minDistance(s))