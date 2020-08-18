# Hadoop-tasks

This repository contains some tasks performed on a Hadoop cluster of computers and addressed with a Map & 
Reduce paradigm over some Big Data files.

The first task implements a simple words and lines count, dividing the document in lines and counting the number of words for each of them. Then the reducer adds the number into two final accumulators.

The second task implements a bi-grams count and their frequencies. At first the documents is divided in bigrams, then they are mapped to count partial frequencies and at then the reducer adds all the partial frequencies into the final ones.

The last task is performed on a movie database and it finds the average rating achieved for movies released
in each decade in a specific time lapse. In order to address the problem two different Map and Reduce jobs
are used where the first prepares the data used as input in the second one.
