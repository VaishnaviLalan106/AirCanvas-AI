import cv2

# Open the default webcam
camera = cv2.VideoCapture(0)

# Keep showing frames until user exits
while True:

    # Capture one frame
    success, frame = camera.read()

    # If camera fails
    if not success:
        print("Couldn't access camera.")
        break

    # Show the frame
    cv2.imshow("AirCanvas AI", frame)

    # Press Q to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release camera
camera.release()

# Close all windows
cv2.destroyAllWindows()