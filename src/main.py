import cv2
import mediapipe as mp
import numpy as np

# -----------------------------
# Create MediaPipe hand detector
# -----------------------------

mp_hands = mp.solutions.hands

hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=1,
    min_detection_confidence=0.8,
    min_tracking_confidence=0.8
)
previous_x = 0
previous_y = 0
lost_frames = 0
# Drawing utility

mp_draw = mp.solutions.drawing_utils

# Open webcam

camera = cv2.VideoCapture(0)

ret, frame = camera.read()
canvas=np.zeros_like(frame)
while True:

    success, frame = camera.read()

    if not success:
        break

    # Mirror the webcam

    frame = cv2.flip(frame, 1)

    # Convert BGR to RGB

    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Detect hands

    results = hands.process(rgb_frame)

    # If a hand exists
    if results.multi_hand_landmarks:

        for hand_landmarks in results.multi_hand_landmarks:

            mp_draw.draw_landmarks(
            frame,
            hand_landmarks,
            mp_hands.HAND_CONNECTIONS
        )

            index_tip = hand_landmarks.landmark[8]
            index_joint = hand_landmarks.landmark[6]
            middle_tip = hand_landmarks.landmark[12]
            middle_joint = hand_landmarks.landmark[10]

            ring_tip = hand_landmarks.landmark[16]
            ring_joint = hand_landmarks.landmark[14]

            pinky_tip = hand_landmarks.landmark[20]
            pinky_joint = hand_landmarks.landmark[18]
            index_up = index_tip.y < index_joint.y

            middle_up = middle_tip.y < middle_joint.y

            ring_up = ring_tip.y < ring_joint.y

            pinky_up = pinky_tip.y < pinky_joint.y
            
            drawing_mode = (
            index_up
            and not middle_up
            and not ring_up
            and not pinky_up
            )
            eraser_mode = (
            index_up
            and middle_up
            and not ring_up
            and not pinky_up
            )

            h, w, _ = frame.shape

            x = int(index_tip.x * w)
            y = int(index_tip.y * h)

            cv2.circle(frame, (x, y), 10, (255, 0, 0), -1)

            if previous_x == 0 and previous_y == 0:
                previous_x = x
                previous_y = y

            if drawing_mode:

                cv2.putText(
        frame,
        "DRAW",
        (20,50),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (255,0,255),
        3
    )

                if previous_x == 0 and previous_y == 0:
                    previous_x = x
                    previous_y = y

                cv2.line(
        canvas,
        (previous_x, previous_y),
        (x, y),
        (255,0,255),
        8
    )

                previous_x = x
                previous_y = y
            elif eraser_mode:

                cv2.putText(
        frame,
        "ERASER",
        (20,50),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0,0,255),
        3
    )

                if previous_x == 0 and previous_y == 0:
                    previous_x = x
                    previous_y = y

                cv2.line(
        canvas,
        (previous_x, previous_y),
        (x, y),
        (0,0,0),
        40
    )

                previous_x = x
                previous_y = y

            else:

                lost_frames += 1

                if lost_frames > 3:
                    previous_x = 0
                    previous_y = 0  
    frame = cv2.add(frame, canvas)
    cv2.imshow("AirCanvas AI", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

camera.release()
cv2.destroyAllWindows()