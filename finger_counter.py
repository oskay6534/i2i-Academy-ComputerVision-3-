import cv2
import mediapipe as mp


mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils


cap = cv2.VideoCapture(0)


with mp_hands.Hands(
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
) as hands:

    while cap.isOpened():
        success, frame = cap.read()
        if not success:
            print("Kamera görüntüsü alınamadı!")
            break


        frame = cv2.flip(frame, 1)
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        

        results = hands.process(rgb_frame)

        total_fingers = 0


        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:

                mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)


                finger_tips = [8, 12, 16, 20]
                finger_pip_joints = [6, 10, 14, 18]

                open_fingers = []


                if hand_landmarks.landmark[4].x > hand_landmarks.landmark[3].x:
                    open_fingers.append(1)
                else:
                    open_fingers.append(0)


                for i in range(4):
                    if hand_landmarks.landmark[finger_tips[i]].y < hand_landmarks.landmark[finger_pip_joints[i]].y:
                        open_fingers.append(1)  # Parmak açık
                    else:
                        open_fingers.append(0)  # Parmak kapalı


                total_fingers = sum(open_fingers)


        cv2.putText(
            frame, 
            f'Fingers: {total_fingers}', 
            (50, 80), 
            cv2.FONT_HERSHEY_SIMPLEX, 
            2, 
            (0, 255, 0),
            3, 
            cv2.LINE_AA
        )


        cv2.imshow('i2i Academy Finger Counter', frame)


        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()