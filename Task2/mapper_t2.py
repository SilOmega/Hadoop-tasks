# mapper.py
import sys


def map_function(document):
    partial_bigram = ""  # use this variable to store the first word of bigram
    for word in document.strip().split():
        if partial_bigram == "":
            partial_bigram = word
        else:
            bigram = partial_bigram + "_" + word
            partial_bigram = word
            yield bigram, 1


for line in sys.stdin:
    for key, value in map_function(line):
        print(key + "\t" + str(value))
