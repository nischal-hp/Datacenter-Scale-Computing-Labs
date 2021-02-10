#!/usr/bin/env python
"""mapper3.py"""
import sys

# The input for this Mapper is the apat63_99.txt file and also the output from the previous Mapper File
for line in sys.stdin:
    line = line.strip()
    # Split each element in a line based on ","
    eachElement= line.split(",")
    # Below condition is triggered if input is from the previous Mapper stage
    if(len(eachElement)==2):
        # Print out the Citing Number and the Count
        print('%s\t%s' %(eachElement[0],eachElement[1]))
    # Below condition is triggered if input is from apat63_99.txt file
    else:
        # Print out all the fields from the apat63_99.txt file
        print('%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s' %(eachElement[0],eachElement[1],eachElement[2],eachElement[3],eachElement[4],eachElement[5],eachElement[6],eachElement[7],eachElement[8],eachElement[9],eachElement[10],eachElement[11],eachElement[12],eachElement[13],eachElement[14],eachElement[15],eachElement[16],eachElement[17],eachElement[18],eachElement[19],eachElement[20],eachElement[21],eachElement[22]))


