#!/usr/bin/python2.7
# mapper.py
import sys

def map_function(document):
    line = document.strip()
    decade, avg = line.split("\t", 1)
    yield decade, avg

for line in sys.stdin:
    for key, value in map_function(line):
        print(key + "\t" + value)