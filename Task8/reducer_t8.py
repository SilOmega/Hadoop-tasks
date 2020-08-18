#!/usr/bin/python2.7
# reducer.py
import sys

prev_id = ""
prev_avg = 0.0
prev_decade = 0
prev_identifier = -1
for line in sys.stdin:
    line = line.strip()
    id_film, id_table, value = line.split("\t", 2)
    id_table = int(id_table)  # this value can be 1 or 2 to indicate input file provenience

    # join of tables on id_film
    if prev_identifier == 1:
        if id_table == 1:  # prev film doesn't have a rating, so discard it
            prev_identifier = id_table
            prev_id = id_film
            prev_decade = int(value)
        else:
            if prev_id == id_film: # prev film is same as current so we merge data about this film
                prev_avg = float(value)
                prev_identifier = id_table
                prev_id = id_film
            else:  # prev film and current film have only one row, both invalid so discarded with counter reset
                prev_identifier = -1

    elif prev_identifier == 2:
        if id_table == 1:  # prev film has all data so print its (decade, avg) pair and update counters
            print(str(prev_decade) + "\t" + str(prev_avg))
            prev_id = id_film
            prev_identifier = id_table
            prev_decade = value
        else:  # prev film has all data so print it (decade, avg) pair and discard current invalid line
            print(str(prev_decade) + "\t" + str(prev_avg))
            prev_identifier = -1

        prev_avg = 0

    if prev_identifier == -1 and id_table == 1:  # initialize only at first valid line
        prev_id = id_film
        prev_decade = int(value)
        prev_identifier = id_table

