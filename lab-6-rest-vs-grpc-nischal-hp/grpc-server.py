# import the required libraries
import io
import grpc_pb2
import grpc_pb2_grpc
import grpc
from concurrent import futures
import time
from PIL import Image
# Add Service which returns back the sum of two integers
class addServiceServicer(grpc_pb2_grpc.addServiceServicer):
    def add(self, request, context):
        # Get the response
        response=grpc_pb2.addMessage()
        response.x=request.x +request.y
        # Return the response
        return response
# Image service which returns the width, height of image
class imageServiceServicer(grpc_pb2_grpc.imageServiceServicer):
    def image(self, request, context):
        # Get the response
        response=grpc_pb2.addMessage()
        response.x,response.y=Image.open(io.BytesIO(request.img)).size[0],Image.open(io.BytesIO(request.img)).size[1]
        # Return the response
        return response    
# create a gRPC server with max workers of 9
grpcServer = grpc.server(futures.ThreadPoolExecutor(max_workers=9))
grpc_pb2_grpc.add_addServiceServicer_to_server(addServiceServicer(), grpcServer)
grpc_pb2_grpc.add_imageServiceServicer_to_server(imageServiceServicer(), grpcServer)
# Add the port on the required IP address
grpcServer.add_insecure_port('10.156.0.2:5000')
# Start the grpc Server
grpcServer.start()