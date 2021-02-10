#!/usr/bin/env python
"""mapper.py"""

import sys

# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    words = line.split()
    # increase counters
    for word in words:
        # write the results to STDOUT (standard output);
        # what we output here will be the input for the
        # Reduce step, i.e. the input for reducer.py
        #
        # tab-delimited; the trivial word count is 1
        # Consider only those words which have a string of "href" present in them, as they indicate a URL
        if "href" in word:
            # Extract out the text present between two double quotes which indicates the required URL
            print('%s\t%s' % (word.split('"', 1)[1].split('"')[0], 1))
