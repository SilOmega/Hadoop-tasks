# mapper.py
import sys

for line in sys.stdin:
    fields = line.strip().split("\t")
    if len(fields) == 9:  # processing a film.basics.tsv line
        if fields[5] != "\N":  # filter all films released between 1900 - 1999
            releaseYear = int(fields[5])
            if 1900 <= releaseYear < 2000:
                decade = (releaseYear / 10) * 10
                id_film = fields[0]
                print(id_film + "\t" + "1" + "\t" + str(decade))   # encode a pair (id_film 1 decade)

    else:
        id_film = fields[0]
        avgRate = fields[1]
        print(id_film + "\t" + "2" + "\t" + avgRate)  # encode a pair (id_film 2 averageRate)
