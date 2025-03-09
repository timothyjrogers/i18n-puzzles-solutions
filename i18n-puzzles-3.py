INPUT_FILE = 'i18n-puzzles-input-3.txt'

with open(INPUT_FILE, 'r', encoding='utf-8') as f:
    data = [x.strip() for x in f.readlines()]

valid_passwords = 0
for d in data:
    if len(d) < 4 or len(d) > 12:
        print("{} : invalid".format(d))
        continue
    found_upper = False
    found_lower = False
    found_digit = False
    found_extended = False
    for c in d:
        if not found_upper and c.isupper():
            found_upper = True
        if not found_lower and c.islower():
            found_lower = True
        if not found_digit and c.isdigit():
            found_digit = True
        if not found_extended and ord(c) >= 128:
            found_extended = True
    if found_upper and found_lower and found_digit and found_extended:
        valid_passwords += 1
        print("{} : valid".format(d))
    else:
        print("{} : invalid".format(d))
print(valid_passwords)