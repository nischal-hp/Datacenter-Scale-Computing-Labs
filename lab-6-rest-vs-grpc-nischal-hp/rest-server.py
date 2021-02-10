# Import required libraries
from PIL import Image
import io
from flask import Flask, request, Response
import jsonpickle
# Initialize the Flask application
app = Flask(__name__)
# Route add endpoints to the below function
@app.route('/api/add/<int:A>/<int:B>' , methods=['GET'])
def add(A,B):
    # Return the response back by summing up the two integers, and also send back the proper status code
    return Response(response=jsonpickle.encode({ 'Sum of Numbers' : A+B}), status=200,mimetype="application/json")
# Route Image endpoint to the below function
@app.route('/api/image', methods=['POST'])
def image():
    # convert the data to a PIL image type so we can extract dimensions
    flatironsImage = Image.open(io.BytesIO(request.data))
    # Return the response back specifying width-height of image, and also send back the proper status code
    return Response(response=jsonpickle.encode({'width' : flatironsImage.size[0],'height' : flatironsImage.size[1] }), status=200, mimetype="application/json") 
# start flask app on the internal IP address of the VM Instance and specific port which is 5000 in this case
app.run(host="10.156.0.2", port=5000)