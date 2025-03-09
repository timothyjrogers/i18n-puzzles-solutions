from datetime import datetime, timezone

INPUT_FILE = 'i18n-puzzles-input-2.txt'

with open(INPUT_FILE, 'r', encoding='utf-8') as f:
    data = [x.strip() for x in f.readlines()]

pings = {}
for d in data:
    dt_normalized = datetime.fromisoformat(d).astimezone(timezone.utc)
    if dt_normalized in pings:
        pings[dt_normalized] += 1
        if pings[dt_normalized] == 4:
            print(dt_normalized.isoformat())
            break
    else:
        pings[dt_normalized] = 1