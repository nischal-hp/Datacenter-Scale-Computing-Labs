# Import the required libraries
import grpc
import sys
from time import perf_counter
import grpc_pb2
import grpc_pb2_grpc
import struct
# Get the number of iterations
numberIterations = int(sys.argv[3])
# Open the Flatirons Image file
flatironsImage = open('Flatirons_Winter_Sunrise_edit_2.jpg', 'rb').read()
# open gRPC insecure channel on the specified IP address
channel = grpc.insecure_channel(str(sys.argv[1]))
# If add endpoint is triggered
if(sys.argv[2] == 'add'):
    count = 1
    # Start counting time
    startTime = perf_counter()
    # Repeat the process for defined number of iterations
    while(count <=numberIterations):
        # Get the response
        response = grpc_pb2_grpc.addServiceStub(channel).addService(grpc_pb2.addMessage(a=9,b=6))
        # Print the response
        print(response.x)
        count+=1
    # Stop counting time
    stopTime = perf_counter()
    # Print out the average response
    print((stopTime - startTime)/numberIterations)
# If Image endpoint is triggered
elif(sys.argv[2]=='image'):
    count = 1
    # Start counting time
    startTime = perf_counter()
    # Repeat the process for defined number of iterations
    while(count <=numberIterations):
        # Get the response
        response = grpc_pb2_grpc.imageServiceStub(channel).image(grpc_pb2.imageMessage(img=flatironsImage))
        # Print the response
        print(response.x,response.y)
        count+=1
    # Stop counting time
    stopTime = perf_counter()
    # Print out the average response
    print((stopTime - startTime)/numberIterations)
else:
    print('Enter Proper Query')