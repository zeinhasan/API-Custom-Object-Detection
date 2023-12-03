import os
import numpy as np
from flask import Flask, render_template, request, jsonify
import function
import random
import torch
import cv2
from io import BytesIO

app=Flask(__name__)

@app.route("/predict", methods=['GET', 'POST'])
def predict(image):
    if request.method == 'POST':
        # Assuming the image is sent as a file with key 'image'
        img_file = request.files['image']
        img = cv2.imdecode(np.frombuffer(img_file.read(), np.uint8), cv2.IMREAD_COLOR)
        img = cv2.resize(img, (416, 416))
        
        # Run YOLO on the image and get annotated image
        yolo_results, annotated_img = function.yolo(img)

        # Convert annotated image to stream 
        img_stream = cv2.imencode('.jpg', annotated_img)[1].tobytes()
        
        # Return the results and annotated image as JSON
        return jsonify({"results": yolo_results, "annotated_image": img_stream.decode('latin1')})


if __name__ == '__main__':
    app.run(debug=True)