# Phase 16 - Save Drawings

## What I Learned

In this phase, I added the ability to save my drawings permanently.

Instead of losing the artwork when closing the application, I used OpenCV's `cv2.imwrite()` function to save the canvas as an image.

I also learned how to automatically create a folder using Python's `os.makedirs()` so the application prepares its own workspace without requiring manual setup.

To avoid overwriting previous drawings, I used a counter (`save_count`) that generates unique file names like:

- drawing_1.png
- drawing_2.png
- drawing_3.png

This helped me understand how simple file management can improve the user experience.

---

## Problems I Faced

### Drawing Quality

While testing, I noticed my hand drawings weren't as smooth as many online AirCanvas demonstrations.

### What I Learned

This is expected because hand tracking quality depends on lighting, webcam quality, frame rate, and smoothing algorithms. My application already performs real-time hand detection and drawing correctly, and I plan to improve the smoothness in a later polishing phase.

---

## New Features

- Save drawings as PNG images.
- Automatically create a drawings folder.
- Save multiple drawings without replacing previous ones.

---

## My Progress

My AirCanvas application can now:

- Draw using hand gestures.
- Erase drawings.
- Change brush colors.
- Clear the canvas.
- Save artwork as image files.

Each phase is making the project feel more like a complete desktop application rather than a simple computer vision experiment.