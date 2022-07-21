import sys
import re

WORD_RE = re.compile(r'\w+')

index = {}

with open(sys.argv[1], 'r', encoding = 'utf-8') as fp:
    for line_no, line in enumerate(fp, start = 1):
        for match in WORD_RE.finditer(line):
            word = match.group()
            column_no = match.start() + 1
            location = (line_no, column_no)
            index.setdefault(word, []).append(location)

#Print index
for word in index:
    print(word, index[word])