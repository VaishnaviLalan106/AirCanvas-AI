# Phase 6 – Creating a Permanent Drawing Canvas

Until now, I was drawing directly on the webcam frame.

The webcam frame refreshes every time a new image is captured, so the drawing disappeared instantly.

To solve this, I created a separate image called `canvas`.

The canvas has the same size as the webcam frame but starts completely black.

Instead of drawing on the webcam frame, I now draw on the canvas.

Finally, I combine the webcam frame and the canvas using `cv2.add()`.

This makes the drawings remain on the screen while the live camera continues updating underneath.

This is the core idea behind many digital drawing applications.