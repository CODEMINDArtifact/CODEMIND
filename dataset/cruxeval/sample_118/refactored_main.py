text = 'zbzquiuqnmfkx'
chars = 'mk'
num_applies = 2
extra_chars = ''
for i in range(num_applies):
    extra_chars += chars
    text = text.replace(extra_chars, '')
print(text)