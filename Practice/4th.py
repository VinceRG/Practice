text = "abcdef"

def two_apart():
    total = 0
    for i in range(len(text) - 2):
        j = i + 2
        total += abs(ord(text[i]) - ord(text[j]))
    return total

result = two_apart()
print(result)
