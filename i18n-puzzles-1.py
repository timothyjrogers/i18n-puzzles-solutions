INPUT_FILE = 'i18n-puzzles-input-1.txt'

with open(INPUT_FILE, 'r', encoding='utf-8') as f:
    data = [x.strip() for x in f.readlines()]

total = 0
for d in data:
    chars = len(d)
    bytes = len(d.encode('utf-8'))
    if chars <= 140 and bytes <= 160:
            total += 13
    elif chars <= 140:
            total += 7
    elif bytes <= 160:
            total += 11

print(total)