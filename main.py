import mss
import numpy as np
import cv2
import torch
import requests
import pandas as pd

# Load the YOLOv5 model with CUDA
model = torch.hub.load('ultralytics/yolov5', 'yolov5s').cuda()

# Initialize screen capture
with mss.mss() as sct:
    monitor = sct.monitors[1]  # Adjust if you have multiple monitors

    while True:
        # Capture screen
        img = np.array(sct.grab(monitor))

        # Convert the image to RGB
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)

        # Perform object detection
        results = model(img_rgb, size=640)

        # Draw bounding boxes and labels
        results.render()

        # Display the image
        cv2.imshow('Screen', results.imgs[0])

        # Exit on pressing 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# Clean up
cv2.destroyAllWindows()
