text = "abcdef"

def score():
    sum = 0 
    for i in range(len(text) - 1):
        letter = text[i]
        next_letter = text[i + 1]
        sum += (abs(ord(letter) - ord(next_letter)))
    return sum

result = score()
print(result)
