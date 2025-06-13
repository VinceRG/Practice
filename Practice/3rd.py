text = "abcdef"

def even_odd():
        diff = 0
        for i in range(0 , len(text) -1 , 2):
            diff +=  abs(ord(text[i]) - ord(text[i + 1]))
        return diff

result = even_odd()
print(result)
