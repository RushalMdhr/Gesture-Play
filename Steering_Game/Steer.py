import cv2
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
from Maths import *
from Kbht import *

# Download this file: https://storage.googleapis.com/mediapipe-models/gesture_recognizer/gesture_recognizer/float16/1/gesture_recognizer.task
GESTURE_MODEL_PATH = '../gesture_recognizer.task'

# Setup Gesture Recognizer in VIDEO mode
base_options = python.BaseOptions(model_asset_path=GESTURE_MODEL_PATH)
options = vision.GestureRecognizerOptions(
    base_options=base_options,
    running_mode=vision.RunningMode.VIDEO,
    num_hands=2,
    min_hand_detection_confidence=0.5,
    min_hand_presence_confidence=0.5,
    min_tracking_confidence=0.5
)

cap = cv2.VideoCapture(0)

with vision.GestureRecognizer.create_from_options(options) as recognizer:
    movement='none'
    Accelerate,Reverse = False,False
    left,right = (0,0),(0,0)
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        frame = cv2.flip(frame, 1)
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb)
        
        # Get timestamp
        timestamp = int(cap.get(cv2.CAP_PROP_POS_MSEC))
        
        # Detect gesture
        result = recognizer.recognize_for_video(mp_image, timestamp)
        
        # Get gesture info
        gesture_name = "No hand detected"
        confidence = 0.0
        if result.gestures:
            gesture = result.gestures[0][0]
            for idx, hand_landmark in enumerate(result.hand_landmarks):
                for landmark in hand_landmark:
                    x = int(landmark.x * frame.shape[1])
                    y = int(landmark.y * frame.shape[0])
                    cv2.circle(frame, (x, y), 3, (0, 255, 0), -1)

            if len(result.hand_landmarks)==2:
                for idx, hand_landmarks in enumerate(result.hand_landmarks):
                    handedness = result.handedness[idx][0].category_name  # 'Left' or 'Right'
                    print(f"Hand {idx}: {handedness}")
                    if handedness=='Right':
                        right=result.hand_landmarks[idx]
                    elif handedness=='Left':
                        left=result.hand_landmarks[idx]
                print("__________________________ left : ",left[9].x,right[9].x)
                mid_X, mid_Y, left_X, left_Y, right_X , right_Y = getMidPoint(right,left)
                mid_X,left_X,right_X,mid_Y,left_Y,right_Y = int(mid_X* frame.shape[1]),int(left_X* frame.shape[1]),int(right_X* frame.shape[1]),int(mid_Y* frame.shape[0]),int(left_Y* frame.shape[0]),int(right_Y* frame.shape[0])
                cv2.circle(frame, (mid_X,mid_Y), 10, (0, 255, 0), -1)
                cv2.line(frame, (mid_X-150,mid_Y), (mid_X+150,mid_Y), (0,0,255), 1)
                cv2.line(frame, (left_X,left_Y), (right_X,right_Y), (0,0,255), 1)
                angle = getAngle(mid_X-150,mid_Y,mid_X+150,mid_Y,left_X,left_Y,right_X,right_Y)
                print("angle : ",angle)
                result = control(angle,movement)
                movement = result
                print("Detected Gestures:", gesture.category_name, "with confidence:", gesture.score)
                if gesture.category_name=='Open_Palm' and Accelerate or Reverse and gesture.category_name=='Open_Palm':
                    releaseAll()
                    Accelerate=False
                    Reverse=False
                elif gesture.category_name=='Victory' and not Reverse:
                    goReverse()
                    Accelerate=False
                    Reverse=True
                elif gesture.category_name=='Closed_Fist' and not Accelerate:
                    pressAcc()
                    Accelerate=True
                    Reverse = False

            else:
                releaseAll()
                print("Not Steering Keep Only 2 hands !")
        else:
            left,right = (0,0),(0,0)
                    
        
        cv2.imshow('Gesture Tester - Try All Gestures!', frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()