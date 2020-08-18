# mapper.py
import sys

lines = 0

def map_function(document):
    words = 0
    for word in document.strip().split():
        words += 1
    yield words, 1


for line in sys.stdin:
    lines += 1
    # Line are keys in this mapper
    for key, value in map_function(line):
        print(str(lines) + "\t" + str(key))
