#!/usr/bin/python

from collections import defaultdict
import math
import sys
prob_dict = defaultdict(lambda: 0)

s1 = 0.95
sunk = 1 - s1
V = 1000000
W = 0
H = 0
unk = 0
#
model_file = open("train.txt", "r")
for line in model_file:
    line = line.strip()
    word_prob = line.split("    ")
    prob_dict[word_prob[0]] = float(word_prob[1])
    

test_file = open(sys.argv[1], "r")

for line in test_file:
    line = line.strip()
    words = line.split(" ")
    words.append("</s>")
    for w in words:
        W += 1
        P = sunk / V
        if prob_dict[w] != 0:
            P =P + s1 * prob_dict[w]
        else:
            unk += 1
        H +=(-math.log(P, 2))

result_file = open("test_result.txt", "w")
result_file.write("entropy = %f\ncoverage = %f" % (H/W, float(W - unk)/W))

