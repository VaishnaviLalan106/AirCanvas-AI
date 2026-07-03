# Phase 7 – UI Toolbar, Save Feature & Debugging

Today was one of the biggest learning days of this project.

## What I added

- Toolbar at the top
- Color palette
- Clear button
- Save button
- Saved drawings as PNG images

## Problems I faced

### 1. MediaPipe didn't recognize `mp.solutions`
Reason:
- Python 3.14 wasn't fully compatible with the version I was using.

Solution:
- Created a fresh virtual environment using Python 3.12.

---

### 2. Drawing wasn't smooth

Reason:
- I was connecting points even when my finger wasn't really in drawing mode.

Solution:
- Reset previous coordinates whenever drawing mode ended.

---

### 3. Open hand was drawing

Reason:
- I was checking only the index finger.

Solution:
- Added gesture logic so drawing happens only when:
- Index finger is up
- Middle, ring and pinky are folded

---

### 4. Eraser sometimes drew purple lines

Reason:
- Drawing and erasing conditions overlapped.

Solution:
- Separated gesture logic and reset previous coordinates properly.

---

### 5. SAVE button wasn't working

Reason:
- The SAVE code was accidentally indented inside the CLEAR button block.

Python indentation decides program flow, so the save code never executed.

Solution:
- Moved the SAVE block outside the CLEAR block.

---

## Biggest lesson today

Small indentation mistakes can completely change program behavior.

I also learned that debugging isn't about guessing—it's about checking one thing at a time until the real cause is found.