# coding=utf-8

import json
import sys
import collections
import dateparser
import math

"""
Data cleaning script
Input: dirty JSON from convert.js on stdin
Args: Facebook username, minimum number of messages for conversation to be considered
Output: cleaned JSON

Example:
node convert.js messages.html | python3 data_clean.py "John Doe" 1000 > messages-clean.json
"""

my_name = sys.argv[1]
min_msg_count = int(sys.argv[2])

print("DATA CLEANER STARTED")
print("User name: "+my_name)
print("Drop conversations with less messages than: "+min_msg_count)
print("Warnings from dateparser will occur, but everything is fine.")
print("The process may take a while, time to watch a silly video on YouTube.")


def parsedate(txt):
    # May (=will) break with some other locales
    (d, m, y, v, t, z) = txt.split()
    return dateparser.parse(" ".join([d, m, y, t]), settings={'TIMEZONE': z})

data = json.loads(sys.stdin.read())

new_data = collections.defaultdict(lambda: [])

for block in data:
    # Remove references to self
    name = block['users'].replace(my_name+", ", "").replace(", "+my_name, "")

    # Remove multiconversations or self
    if "," in name or name == my_name:
        continue

    new_msg = [{
        'by_me': m['user'] == my_name,
        'text': m['text'],
        'date': math.floor(parsedate(m['date']).timestamp())
        } for m in block['messages']]

    new_data[name] = new_msg + new_data[name]

sys.stdout.write(json.dumps({k: v for k, v in new_data.items() if len(v) > min_msg_count}, indent=2, ensure_ascii=False, sort_keys=True))
