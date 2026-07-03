# Phase 7 – Adding Smart Drawing Mode

Previously, the program drew whenever it detected my hand.

This made it impossible to move my hand without creating unwanted lines.

To solve this, I used the position of the index finger tip and its joint.

If the fingertip is above the joint, the finger is considered "up", so drawing mode is enabled.

If the finger is folded, drawing mode is disabled.

When drawing mode is disabled, I reset the previous drawing coordinates. This prevents unwanted long lines when drawing starts again.

This simple gesture makes the Air Canvas much easier and more natural to use.