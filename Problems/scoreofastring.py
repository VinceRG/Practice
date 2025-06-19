s = "hello"
total = 0
def sum(s,total):
    for i in range(len(s) - 1):
        total += abs(ord(s[i]) - ord(s[i + 1]))
    return total

print(sum(s,total))