def lengthOfLongestSubstring(self, s: str) -> int:
    ls = []
    l = len(s)
    if l == 1:
        return 1
    if l == 2:
        if s[0] == s[1]:
            return 1
        else:
            return 2
    for i in range(l):
        for j in range(i + 1, l):
            if s[j] in s[i: j]:
                ls.append(s[i: j])
                break
            if s[j] not in s[i: j] and j == l - 1:
                ls.append(s[i: j + 1])
    los = 0
    for sub in ls:
        los = max([los, len(sub)])

    return los


print(lengthOfLongestSubstring("abcabcbb"))