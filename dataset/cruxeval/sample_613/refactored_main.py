text = 'eat!'
result = ''
mid = (len(text) - 1) // 2
for i in range(mid):
    result += text[i]
for i in range(mid, len(text)-1):
    result += text[mid + len(text) - 1 - i]
print(result.ljust(len(text), text[-1]))