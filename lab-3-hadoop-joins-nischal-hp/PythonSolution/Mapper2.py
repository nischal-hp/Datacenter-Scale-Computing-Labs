#!/usr/bin/env python
"""mapper2.py"""
import sys

# Mapper2 takes in the apat63_99.txt file and the output from the previous Mapper1.py stage
for line in sys.stdin:
    line = line.strip()
    # Split based on the ","
    eachLineElement = line.split(",")
    # Below condition is triggered if the input is from apat63_99.txt file
    if len(eachLineElement) != 3:
        # Extract out the patent name and the state name
        patentName,patentState = eachLineElement[0],eachLineElement[5]
        # Print out the patent name and the corresponding state name
        print('%s\t%s' %(patentName,patentState))
    # Below condition is triggered if the input is from previous Mapper stage
    else:
        # Extract out the Citing name and the Cited State name
        citingName,citedStateLocation = eachLineElement[1], " ".join([eachLineElement[0], eachLineElement[2]])
        # Print out the Citing name and the corresponding state name
        print('%s\t%s' %(citingName,citedStateLocation))





