#!/usr/bin/python2.7
# reducer.py
import sys


counter = 0
prev_decade = ""
partial_rate = 0.0

for line in sys.stdin:
    line = line.strip()
    decade, rate = line.split("\t", 1)
    decade, numFilms = decade.split("_", 1)
    numFilms = int(numFilms)
    rate = float(rate)

    if prev_decade == decade:
        partial_rate += rate
        counter += numFilms
    else:
        if counter != 0:
            total_avg = round(partial_rate / counter, 1)
            print(prev_decade + "\t" + str(total_avg))
            counter = numFilms
            partial_rate = rate
            prev_decade = decade
        else:
            prev_decade = decade
            partial_rate = rate
            counter = numFilms

if prev_decade != "":
    total_avg = round(partial_rate / counter, 1)
    print(prev_decade + "\t" + str(total_avg))