# Assignment #3 - Data Joins in Hadoop - Solution

I did the Python implementation for this lab. I ended up using 3 Mapper-Reducer stages in total, to get the Final output.
### Mapper1.py
This mapper takes in the input from the two files - apat and cite text files. The main goal of this mapper is to send the data across to the Reducer in the following format - "CITED, CITING, LOCATION". If the input is from the apat text file, then we get just the Cited and the Location Info. Thus for Citing we would just output an hyphen. If the input is from the cite text file, then we get just the Cited and the Citing Info. Thus for Location we would output an hyphen again.
### Reducer1.py
The input to this comes from the Mapper1.py output. The main goal of the Reducer is to output out the data in the following format - "CITED, CITING, LOCATION". From the presence of hyphens we can make out whether the location or the citing information is missing. Since, the Reducer stage gets the sorted input based on key values, I could detect the presence of new Key; which indicates that we are moving onto the next Cited Paper. Thus processing could be made for each of the Cited papers individually.
### Mapper2.py
This mapper takes in the input from the two files - apat text file and the previous Mapper1 ouput. If the input is from the apat text file, I extract out the patent name and the state; and send it across to theReducer stage. If the input is from the previous Mapper file, I send out the Citing paper name as the Key; and the values would be the Cited paper and the Location Information.
### Reducer2.py
The input to this comes from the Mapper2.py output. I made use of the Helper code provided to implement this Reducer. Thus, the values for the same Key would be combined into a single list. If this combined list contains a single element, then it indicates the state of the Citing Paper. Using this information, I then traversed through the other elements if their state info matches the Citing Paper state info. Based on the previous condition, a counter is incremented. Thus, the final output from this reducer is of the Form - Citing, Count. 
### Mapper3.py
This mapper takes in the input from the two files - apat text file and the previous Mapper2 ouput. If the input is from the previous Mapper stage, I send it out by splitting the elements and then making them tab-separated. If the input is from the apat text file, then 
all the fields are sent across by splitting them and making them tab separated.
### Reducer3.py
The input to this comes from the Mapper3.py output. I made use of the Helper code provided to implement this Reducer. Thus, the values for the same Key would be combined into a single list. There are chances that sometimes, the same state citation count appears at the very beginning of the list, instead of the in the end of the list as required. Thus, this condition is checked for in the Reducer stage;
and the element in popped out and inserted at the end of the list if that is the case. The final output is of the specified format. This output is checked by comparing them with the given reference values.
