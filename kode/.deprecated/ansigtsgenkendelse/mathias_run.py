import cv2
import numpy as np

# Load the LBPH face recognizer
recognizer = cv2.face.LBPHFaceRecognizer_create()

# Load the trained model
recognizer.read('model.yml')

# Load the Haar cascades for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Initialize the camera
cap = cv2.VideoCapture(0)

while True:
    # Capture a frame from the camera
    ret, frame = cap.read()

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the grayscale frame
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    for (x, y, w, h) in faces:
        # Draw a rectangle around each detected face
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Extract the face ROI (Region of Interest)
        roigray = gray[y:y + h, x:x + w]

        # Recognize the face using the LBPH recognizer
        id, confidence = recognizer.predict(roigray)

        # If the confidence is high enough, display the recognized name
        if confidence < 50:
            # Load the names and ids from the training dataset
            names = []
            with open('names.txt', 'r') as f:
                lines = f.readlines()
                for line in lines:
                    names.append(line.strip())

            # Display the recognized name on the frame
            cv2.putText(frame, names[id], (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

    # Display the frame
    cv2.imshow('Facial Recognition', frame)

    # Exit if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close all windows
cap.release()
cv2.destroyAllWindows()

