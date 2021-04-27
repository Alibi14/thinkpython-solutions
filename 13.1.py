import string

file = open('lipsum.txt')
swears = string.punctuation

full_text = []
for line in file:
    paragraph = line.strip('\n').lower()
    words = paragraph.split(' ')

    if len(words) == 1:
        del words
    else:
        full_text = full_text + words

new_var = ''

for word in full_text:
    for char in swears:
        if char in word:
            word = word.replace(char, '')

    new_var = new_var + word + ' '


print(new_var)
d = {}

for key in new_var:
    if key not in d:
        d[key] = 1
    else:
        d[key] += 1

print(d)

print('lorem ipsum dolor sit amet ')



# i think that't so colse for you motherfucker nn