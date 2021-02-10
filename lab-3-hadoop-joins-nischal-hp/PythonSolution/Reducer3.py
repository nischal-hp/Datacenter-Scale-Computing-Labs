#!/usr/bin/env python
"""reducer3.py"""
from operator import itemgetter
import sys
from itertools import chain

# Helper Code is made use of, for this Mapper

# Below is the main function for this Reducer Stage
def outputFinalResult(key, values):
    new_array,array=[],[]
    for each_value in values:
        # Append the element to the respective array based on its length
        if len(each_value)!=1:
            new_array.append(each_value)
        else:
            array.append(each_value)
    new_array.append(array)
    # Flatten out the array
    newList = list(chain.from_iterable(new_array))
    # If the type of last element is 'List'. Pop it out and append it as a single element
    if type(newList[-1]) is list:
        newElement=newList[-1][0]
        newList.pop()
        newList.append(newElement)
    # Convert each of the elements in the list back to their original form
    for i in range(0, len(newList)): 
        try:
            newList[i] = int(newList[i]) 
        except ValueError:
            continue
    # Strip out the '[]' to get the final output
    finalOutput=str(newList).strip('[]')
    # Print out the Key along with the value in the required format
    print('%s,%s' %(key,finalOutput))


def main():
    current_patent = None
    values = []
    # input comes from STDIN
    for line in sys.stdin:
        line = line.rstrip('\n')

        # parse the input we got from mapper.py
        try:
            key, value = line.split('\t', 1)
            value=value.split('\t')
        except:
            print('Improperly formatted: *', line, '*')
            # Improperly formatted, so ignore
            continue

        # convert count (currently a string) to int
        try:
            patent = int(key)
        except ValueError:
            # key was not a number, so silently
            # ignore/discard this line
            continue

        # this IF-switch only works because Hadoop sorts map output
        # by key (here: word) before it is passed to the reducer

        if current_patent != patent:
            if current_patent:
                outputFinalResult(current_patent, values)
            current_patent = None
            values = []

        current_patent = patent
        values.append(value)
        
    # do not forget to output the last word if needed!
    if current_patent:
        outputFinalResult(current_patent, values)



main()
