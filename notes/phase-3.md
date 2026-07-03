# Phase 3 – Detecting Hands with MediaPipe

Today my application became more than just a webcam viewer. It can now detect a human hand in real time using Google's MediaPipe library.

## What I learned

### MediaPipe

MediaPipe is an AI-powered computer vision library developed by Google. Instead of simply displaying video, it analyzes each frame and identifies important points on a hand called landmarks.

### Hand Landmarks

A detected hand contains 21 landmarks. These landmarks represent important joints such as the wrist, fingertips, and finger joints. Every landmark has a unique number that can be used later for gesture recognition.

### Why convert BGR to RGB?

OpenCV reads images in BGR format, while MediaPipe expects RGB format. Converting the frame before processing ensures the AI model receives the image in the format it was trained on.

### Mirroring the webcam

Flipping the frame horizontally makes the webcam behave like a mirror, creating a much more natural user experience when interacting with the application.

### AI Processing

The `hands.process()` method is where the actual AI inference happens. It examines every frame from the webcam and returns the detected hand landmarks if a hand is present.

## What I realized today

The AI does not recognize fingers directly. Instead, it detects 21 precise points on the hand. Later, I can use the positions of these points to understand gestures, detect finger movements, and allow users to draw in the air.