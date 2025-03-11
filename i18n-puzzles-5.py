INPUT_FILE = 'i18n-puzzles-input-5.txt'

UNICODE_POOP = b'\\U0001f4a9'

with open(INPUT_FILE, 'r', encoding='utf-8') as f:
    data = [x[:-1] for x in f.readlines()]

y = 0
x = 0
total = 0
while y < len(data) - 1:
    if data[y][x].encode('unicode_escape') == UNICODE_POOP:
        total += 1
    y += 1
    x = (x + 2) % len(data[0])
print(total)