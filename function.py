import numpy as np
import cv2
import torch
from google.cloud import storage
from ultralytics import YOLO
import json

# Get the model from the bucket
storage = storage.Client()
bucket = storage.bucket('object-detection-image')
blob = bucket.blob('Apple-YoloV8L.pt')
blob.download_to_filename('Apple-YoloV8L.pt')
model = YOLO('Apple-YoloV8L.pt')

def yolo(img):
    # Assuming you have a YOLO model loaded
    results = model.predict(img)
    result_json = results[0].tojson()
    result_json = json.loads(result_json)
    
    annotated_img = img.copy()
    
    output_list = []
    for i, item in enumerate(result_json, 1):
        label = item["name"]
        confidence = item["confidence"]
        box = item["box"]
        x1, y1, x2, y2 = box["x1"], box["y1"], box["x2"], box["y2"]
        
        bbox = {
            "x1": x1,
            "y1": y1,
            "x2": x2,
            "y2": y2
        }

        output_list.append({
            "name": label,
            "bounding_box": bbox,
            "confidence": confidence
        })
        
        # Draw bounding box on the image
        cv2.rectangle(annotated_img, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)
        cv2.putText(annotated_img, f"{label} {confidence:.2f}", (int(x1), int(y1) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    return output_list, annotated_img