#!/usr/bin/python2.7
# combiner.py
import sys

counter = 0
prev_decade = ""
partial_rate = 0.0

for line in sys.stdin:
    line = line.strip()
    decade, rate = line.split("\t", 1)
    rate = float(rate)

    if prev_decade == decade:
        partial_rate += rate
        counter += 1
    else:
        if counter != 0:
            print(prev_decade + "_" + str(counter) + "\t" + str(partial_rate))
            counter = 1
            partial_rate = rate
            prev_decade = decade
        else:
            prev_decade = decade
            partial_rate = rate
            counter = 1

if prev_decade != "":
    print(prev_decade + "_" + str(counter) + "\t" + str(partial_rate))