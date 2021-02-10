# Import required Libraries
from time import perf_counter
import requests
import json
import sys
# Get the number of Iterations
noIterations = int(sys.argv[3])
# Read in the image file
flatironsImage = open('Flatirons_Winter_Sunrise_edit_2.jpg', 'rb').read()
# Check if add endpoint is triggered
if(sys.argv[2] == 'add'):
    count = 1
    # Start counting time
    startTime = perf_counter()
    # Repeat the process for defined number of iterations
    while(count<=noIterations): 
        # Get the response
        response = requests.get(str(sys.argv[1]) + '/api/add/9/6', headers={'content-type':'text/plain'})
        # Print the response
        print(response)
        count+=1
    # Stop counting time
    stopTime = perf_counter()
    # Print out the average response
    print((stopTime - startTime)/noIterations)
# Check if image endpoint is triggered
elif(sys.argv[2] == 'image'):
    count = 1
    # Start counting time
    startTime = perf_counter()
    # Repeat the process for defined number of iterations
    while(count<=noIterations): 
        # Get the response
        response = requests.post(str(sys.argv[1]) + '/api/image', data=flatironsImage, headers= {'content-type': 'image/png'})
         # Print the response
        print(json.loads(response.text))
        print(response)
        count+=1
    # Stop counting time
    stopTime = perf_counter()
    # Print out the average response
    print((stopTime - startTime)/noIterations)
else:
    print('Enter Proper Query')



