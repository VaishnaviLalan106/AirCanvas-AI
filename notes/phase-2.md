# Phase 2 – Reading Live Video from the Webcam

Today I learned that a webcam doesn't send a continuous "video" to Python. Instead, it sends many individual images called frames. When these frames are displayed one after another very quickly, they appear as smooth motion.

## What I learned

### Opening the webcam

I used `cv2.VideoCapture(0)` to connect to my laptop's default webcam. The value `0` usually refers to the built-in camera.

### Frames

Each time I call `camera.read()`, OpenCV captures one image from the webcam.

That image is called a frame.

A live video is simply a sequence of frames displayed rapidly.

### The while loop

The `while True` loop keeps asking the camera for the next frame over and over again. Without this loop, I would only capture a single image instead of a live video.

### Displaying the frame

The `cv2.imshow()` function opens a window and displays the current frame. Since the frame changes continuously inside the loop, the window appears to show live video.

### Closing the application

When I press the `Q` key, the loop stops. I then release the webcam using `camera.release()` and close all OpenCV windows with `cv2.destroyAllWindows()`.

## What I realized today

A webcam stream is actually just thousands of images shown very quickly. Understanding this makes it easier to understand how computer vision works, because every AI model processes one frame at a time rather than an entire video all at once.