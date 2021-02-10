#!/usr/bin/env python
"""reducer2.py"""
from operator import itemgetter
import sys
from collections import Counter
from itertools import chain
# Helper Code is made use of, for this Mapper

# Below function is used to find out a single element in the list. This inidicates the state of the Citing Paper
# If no state is found, an empty string is returned instead
def find_Single_Element(list):
    for elem in list:
        if len(elem)==1:
            return elem
    return ['']

# Below Function is used to find the Same state count between the Citing and the Cited paper.
def find_occurances(single_elem,alist):
    count=0
    for elem in alist:
        if elem ==single_elem[0]:
            count+=1
    return count

def outputCountInfo(key, values):
    #
    # The input is of the format -  Cited, [[Cited_State],[Citing,State],[Citing,State]]
    #
    new_array=[]
    # Below condition gets rid of those patents which do not cite any other patent
    if len(values)>1:
        # Split each of the element and append it to an array
        for each_value in values:
            value=each_value.split()
            new_array.append(value)
        # Find out the single element in the list, which indicates the state of the Citing paper
        single_value=find_Single_Element(new_array)
        # Flatten out the list
        newlist = list(chain.from_iterable(new_array))
        # Find the Number of same state citations
        no_occurances=find_occurances(single_value,newlist)
        if no_occurances>0:
            # Decrement the count by 1, as it also contains the Citing paper state
            no_occurances=no_occurances-1
            print('%s,%s' %(key,no_occurances))
        else:
            # If there are no same state citations, print out 0
            print('%s,%s' %(key,no_occurances))


def main():
    current_patent = None
    values = []
    # input comes from STDIN
    for line in sys.stdin:
        line = line.rstrip('\n')

        # parse the input we got from mapper.py
        try:
            key, value = line.split('\t', 1)
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
                outputCountInfo(current_patent, values)
            current_patent = None
            values = []

        current_patent = patent
        values.append(value)
        
    # do not forget to output the last word if needed!
    if current_patent:
        outputCountInfo(current_patent, values)



main()
