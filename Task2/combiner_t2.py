#!/usr/bin/python2.7
# combiner.py
import sys

prev_bigram = ""
prev_frequency = 0

for line in sys.stdin:
    line = line.strip()
    bigram, frequency = line.split("\t", 1)
    frequency = int(frequency)

    if prev_bigram == bigram:  # sum partial frequencies for every bigram
        prev_frequency += frequency
    else:
        if prev_bigram != "":
            print(prev_bigram + "\t" + str(prev_frequency))

        prev_frequency = frequency
        prev_bigram = bigram


if prev_bigram != "":
    print(prev_bigram + "\t" + str(prev_frequency))
