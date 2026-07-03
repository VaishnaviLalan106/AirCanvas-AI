# Phase 4 – Detecting the Index Finger

Today I learned that MediaPipe detects 21 landmarks on a hand.

Each landmark has a fixed number.

Landmark 8 represents the tip of the index finger.

MediaPipe gives coordinates in normalized form (between 0 and 1), not pixels.

To draw on the screen, I converted those normalized values into pixel coordinates using the width and height of the webcam frame.

Finally, I drew a blue circle on the fingertip using OpenCV.

This blue circle will become the virtual paint brush in the next phase.