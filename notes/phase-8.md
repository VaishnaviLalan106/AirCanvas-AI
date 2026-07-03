# Phase 7 - Adding an Eraser

Today I taught the application to understand another hand gesture.

Instead of only detecting one raised finger for drawing, I added a second gesture:

• One finger up → Draw
• Two fingers up → Erase

The eraser works by drawing thick black lines over the existing drawing on the canvas. Since the canvas background is black, this creates the illusion of erasing.

I also displayed the current mode ("DRAW" or "ERASER") on the webcam screen so the user always knows what tool is active.

This phase helped me understand that gesture recognition can be mapped to different application tools, making hand tracking much more interactive.