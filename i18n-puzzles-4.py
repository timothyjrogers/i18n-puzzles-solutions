from datetime import datetime
from datetime import timezone as dt_timezone
import re
from pytz import timezone

INPUT_FILE = 'i18n-puzzles-input-4.txt'

TIMEZONE_REGEX = re.compile(r"[A-Z]\w+(?:\/[A-Z][\w-]+)+")
TIMESTAMP_REGEX = re.compile(r"[A-Z][a-z]{2} \d{2}, \d{4}, \d{2}:\d{2}")

with open(INPUT_FILE, 'r', encoding='utf-8') as f:
    data = [x.strip() for x in f.readlines()]

total = 0
departure = None
arrival = None
for d in data:
    if len(d) == 0:
        departure = None
        arrival = None
        continue
    tz = re.findall(TIMEZONE_REGEX, d)[0]
    timestamp = re.findall(TIMESTAMP_REGEX, d)[0]
    if d[0] == 'D':
        departure = timezone(tz).localize(datetime.strptime(timestamp, '%b %d, %Y, %H:%M'))
    if d[0] == 'A':
        arrival = timezone(tz).localize(datetime.strptime(timestamp, '%b %d, %Y, %H:%M'))
        total += (arrival - departure).seconds / 60
print(total)