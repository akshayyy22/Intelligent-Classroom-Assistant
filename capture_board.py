import cv2
import os
import time

def capture_images(output_folder):
    """Captures an image from the camera and saves it to the given output folder."""
    os.makedirs(output_folder, exist_ok=True)  

    cap = cv2.VideoCapture(0)  
    if not cap.isOpened():
        print("Error: Could not open the camera.")
        return

    ret, frame = cap.read()
    if ret:
        timestamp = time.strftime("%Y%m%d-%H%M%S")
        img_path = os.path.join(output_folder, f"blackboard_{timestamp}.jpg")
        cv2.imwrite(img_path, frame)
        print(f"Captured and saved: {img_path}")
    else:
        print("Error: Could not capture an image.")

    cap.release()
