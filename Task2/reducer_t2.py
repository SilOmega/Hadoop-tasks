#!/usr/bin/python2.7
# reducer.py
import sys

prev_bigram = ""
prev_frequency = 0

for line in sys.stdin:
    line = line.strip()
    bigram, frequency = line.split("\t", 1)
    frequency = int(frequency)

    if prev_bigram == bigram:  # sum frequencies for every bigram and print if freq > 5
        prev_frequency += frequency
    else:
        if prev_bigram != "" and prev_frequency > 5:
            print(prev_bigram + " " + str(prev_frequency))

        prev_frequency = frequency
        prev_bigram = bigram


if prev_bigram != "" and prev_frequency > 5:
    print(prev_bigram + " " + str(prev_frequency))

