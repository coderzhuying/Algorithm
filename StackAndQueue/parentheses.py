"""
括号匹配问题
判断一个由括号组成的字符串，括号是否匹配
"""


def isValid(string):
    stack = []
    paren_map = {'}': '{', ']': '[', ')': '('}
    for s in string:
       if s not in paren_map:
           stack.append(s)
       elif not stack or paren_map[s] != stack.pop():
           return False

    return not stack


if __name__ == '__main__':
    print(isValid("()"))