import cv2
import time
from collections import deque
capture = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
print("Enter 'q' to quit the program.")
starting_time = 0
coordinate_points = deque(maxlen=60)
while 1:
    ret,frame = capture.read()
    if not ret :
        print("The frame could not be read!")
        break
    frame = cv2.flip(frame,1)
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 5, minSize=(30, 30))
    if len(faces) > 0:
        (x, y, w, h) = faces[0]
        if starting_time is 0:
             starting_time = time.time()
        elapsed_time = time.time() - starting_time
        cx = x + w//2
        cy = y + h//2
        coordinate_points.append((cx,cy))
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0,255,0), 2)
        cv2.putText(frame, f"Center: ({cx},{cy})", (10, 30),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,255,0), 2)
        height,width = frame.shape[:2]
        cv2.putText(frame,f"Time:{elapsed_time:.2f}",(width - 200, 30),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,0,255),2)
    else:
        starting_time = 0
        coordinate_points.clear()
    for i in range(1,len(coordinate_points)):
        if coordinate_points[i - 1] is None or coordinate_points[i] is None:
            continue
        cv2.line(frame, coordinate_points[i - 1], coordinate_points[i],(0,255,255),2)
    cv2.imshow("Face Tracking",frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
         break
capture.release()
cv2.destroyAllWindows()       