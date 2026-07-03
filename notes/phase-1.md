# Phase 1 – Setting Up the Project

Today I didn't write any code yet, and that was intentional.

Before building anything, I organized the project folder and installed all the libraries I'll need.

## What I learned

### OpenCV

OpenCV lets Python access the webcam and process images. I like to think of it as the "eyes" of the application because it allows the program to see the real world.

### MediaPipe

MediaPipe is Google's library for detecting hands, fingers, faces, and body poses. Instead of creating my own hand detection algorithm, I can use MediaPipe to find the exact position of every finger in real time.

### NumPy

An image isn't magic—it's really just a grid of pixels stored as numbers. NumPy helps Python work with these large grids efficiently, which is why OpenCV depends on it.

### Pillow

Pillow is useful for working with images, icons, and saved drawings. I'll use it later to improve the application's appearance.

### CustomTkinter

The normal Tkinter interface works, but it looks outdated. CustomTkinter lets me create a cleaner and more modern interface with rounded buttons and better styling.

### PyInstaller

When the project is finished, PyInstaller will package everything into a Windows executable (.exe), so people can run it without installing Python.

## What I realized today

I used to think building a project starts by writing code immediately.

Now I understand that preparing the project structure and installing the right tools is also part of software development.

A well-organized project is much easier to maintain and improve later.