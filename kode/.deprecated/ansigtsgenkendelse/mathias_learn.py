import cv2
import os
import numpy as np

# Define the path to the dataset directory
dataset_dir = '/home/benny/pi_reader/ansigtsgenkendelse'
img_path = '/home/benny/pi_reader/ansigtsgenkendelse/faces/Benny.jpg'

# Load the Haar cascades for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Initialize the lists for face features and labels
face_features = []
labels = []

# Loop over the subdirectories in the dataset directory
# for sub_dir in os.listdir(dataset_dir):
#     sub_dir_path = os.path.join(dataset_dir, sub_dir)
#     # Loop over the images in each subdirectory
#     for img_name in os.listdir(sub_dir_path):
#         img_path = os.path.join(sub_dir_path, img_name)
# Load the image and convert it to grayscale
img = cv2.imread(img_path)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Detect the face in the grayscale image
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
for (x, y, w, h) in faces:
    # Extract the face ROI (Region of Interest)
    roi_gray = gray[y:y + h, x:x + w]
    # Resize the face ROI to a fixed size
    roi_gray = cv2.resize(roi_gray, (100, 100), interpolation=cv2.INTER_LINEAR)
    # Add the face features and label to the lists
    face_features.append(roi_gray)
    labels.append(int(2))

# Train the LBPH face recognizer
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.train(face_features, np.array(labels))

# Save the trained model to a file
recognizer.write('model.yml')