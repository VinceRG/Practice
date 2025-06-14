s = "pwwkew"

def longestsubstring():
    res = ""
    temp = ""
    for c in s:
        if c in temp:
            temp = temp[temp.index(c)+1:]
        temp += c
        if len(temp) > len(res):
            res = temp
    return len(res)

print(longestsubstring())