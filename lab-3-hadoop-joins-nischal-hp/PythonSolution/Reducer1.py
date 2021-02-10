#!/usr/bin/env python
"""reducer.py"""
from operator import itemgetter
import sys

# Below variables are used to keep track of the Current Cited Paper
citedPrevious,currentLocation,citingPapers = None,"-",[]
# Take in the input from Mapper1.py
for line in sys.stdin:
    # Obtain the below 3 variables by splitting on each of the lines
    cited, citing, location = [x.strip() for x in line.split('\t')]
    # Below condition is triggered when there is a change in the cited paper
    if cited != citedPrevious:
        # Print out Cited, Citing, Location information for each element in the citingPapers list
        for eachCiting in citingPapers:
            print ('%s,%s,%s' % (citedPrevious,eachCiting,currentLocation))
        # Reset the below 3 variables to indicate the change in the cited paper
        citedPrevious,currentLocation,citingPapers = cited,"-",[]
        # Update the location Information to the current location based on the below condition
        if location and location != "-":
            currentLocation = location
        # Append the Citing to the citingPapers list
        else:
            citingPapers.append(citing)
    # Below condition is triggered when we are looking at the same cited paper
    elif not citedPrevious or citedPrevious == cited:
        citedPrevious = cited
        # Update the location Information to the current location based on the below condition
        if location and location != "-":
            currentLocation = location
        # Append the Citing to the citingPapers list
        else:
            citingPapers.append(citing)
#  Print out Cited, Citing, Location information for the last Cited paper
for eachCiting in citingPapers:
            print ('%s,%s,%s' % (citedPrevious,eachCiting,location))