# Phase 5 – Drawing Lines with the Finger

Today I learned how drawing applications actually create lines.

Instead of drawing only the current fingertip position, I stored the previous position of the index finger.

Every new frame, I connected the previous point to the current point using `cv2.line()`.

The program repeats this many times every second, creating the illusion of a continuous line.

I also learned why the first point needs special handling. If no previous point exists, the program first stores the current position before drawing.

The drawing still disappears because the webcam image refreshes every frame. In the next phase, I'll solve this by creating a separate drawing canvas that preserves everything I draw.