#!/usr/bin/python2.7
# reducer.py
import sys


total_word = 0
total_line = 0

for line in sys.stdin:
	line = line.strip()
	lines, value = line.split("\t", 1)
	lines = int(lines)
	value = int(value)

	total_line += 1
	total_word += value

print(str(total_word) + "\t" + str(total_line))
