#!/usr/bin/env python
"""mapper.py"""
import sys

# Input is from 2 files - apat63_99.txt and cite75_99.txt
for line in sys.stdin:
    # Need to extract out the following three fields
    citing,cited,location = "-","","-"
    # Strip out the newline character
    line = line.rstrip('\n')
    # Split the line into individual words
    try:
        words = line.split(",")
    # Can't split, so invalid line. Just ignore the line
    except:        
       continue

    if len(words) == 2:
        # Means it is a Citing Information
        citing = words[0]
        cited = words[1]            
    else:
        # Means it will be a Patent Information - Extract out just the state and the cited paper information
        cited = words[0]
        location = words[5]  
    # Print out in the following format - CITED, CITING, LOCATION
    print('%s\t%s\t%s' % (cited,citing,location))
