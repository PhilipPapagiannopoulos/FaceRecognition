Real-Time Face Detection with OpenCV

This project is a real-time face detection application built with Python and OpenCV.
It uses Haar Cascade Classifiers to detect human faces through a webcam feed and draw colored bounding boxes around them.

Features
Real-time webcam face detection
Dynamic face counter display
Change bounding box colors using keyboard controls
Capture and save screenshots directly from the webcam
Lightweight and beginner-friendly OpenCV project
Controls
B → Blue bounding boxes
G → Green bounding boxes
R → Red bounding boxes
SPACE → Save current frame as an image
ESC → Exit the application
Technologies Used
Python
OpenCV
Haar Cascade Classifier
How It Works

The program captures live video from the webcam, converts each frame to grayscale, and uses OpenCV’s Haar Cascade face detection model to identify faces. Once detected, rectangles are drawn around the faces and updated continuously in real time.

Requirements
Python 3.x
OpenCV (cv2)
Haar Cascade XML file:
haarcascade_frontalface_default.xml
