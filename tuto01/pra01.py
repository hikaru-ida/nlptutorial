#!/usr/bin/python
from collections import defaultdict
import sys
training_file = open(sys.argv[1], "r")
counts = defaultdict(lambda: 0)
total_count = 0

for line in training_file:
    line = line.strip()
    word_list = line.split(" ")
    word_list.append("</s>")
    for word in word_list:
        counts[word] += 1
        total_count += 1

model_file = open("train.txt", "w")
for word, count in sorted(counts.items()):
    prob = float(counts[word]) / total_count
    model_file.write("%s    %f\n" % (word, prob))

model_file.close()
