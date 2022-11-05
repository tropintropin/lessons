import json


words = []
with open('words.txt', 'r') as f:
    for line in f:
        words.append(line[:-1])

with open('words.json', 'w') as f:
    json.dump(words, f, indent=4, ensure_ascii=False)
