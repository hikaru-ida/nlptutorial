#!/usr/bin/python

from collections import defaultdict
import sys
import re
my_file = open(sys.argv[1], "r")
my_dict = defaultdict(lambda: 0)

for line in my_file:

    line.replace('"',"").replace(' ',"").replace('(',"").replace(')',"")
    line = line.strip()

    if len(line) != 0:
        word_list = line.split(" ");
        
        for word in word_list:
            my_dict[word]+= 1

for key, value in sorted(my_dict.items()):
    print("%s   %d" % (key, value))
