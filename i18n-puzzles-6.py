INPUT_FILE = 'i18n-puzzles-input-6.txt'

def unmangle(s):
    return bytearray(s, encoding='latin-1').decode(encoding='utf-8')

dictionary = []
crossword = []
section = 0
with open(INPUT_FILE, 'r', encoding='utf-8') as f:
    for d in f.readlines():
        if d == '\n':
            section = 1
        if section == 0:
            dictionary.append(d.strip())
        else:
            crossword.append(d.strip())


for d_index in range(len(dictionary)):
    if (d_index + 1) % 3 == 0:
        dictionary[d_index] = unmangle(dictionary[d_index])
    if (d_index + 1) % 5 == 0: # not an elif so % 15 gets unmangled twice
        dictionary[d_index] = unmangle(dictionary[d_index])

answer = 0
for word in crossword:
    length = len(word)
    position = -1
    letter = None
    for i in range(length):
        if word[i] != '.':
            position = i
            letter = word[i]
            break
    for d_index in range(len(dictionary)):
        if len(dictionary[d_index]) == length and dictionary[d_index][position] == letter:
            answer += d_index + 1

print(answer)