import cv2
import djitellopy


tello = djitellopy.Tello()
tello.connect()
tello.streamon()
frame_read = tello.get_frame_read()


face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')


cv2.namedWindow('Tello Video')


tello.takeoff()



tello.move_forward(50)
tello.rotate_clockwise(180)
tello.move_forward(50)

while True:
    frame = frame_read.frame   
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    
    detection_rate = len(faces)
    cv2.putText(frame, f"Face Detection: {detection_rate}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.imshow('Tello Video', frame)

    

    if cv2.waitKey(1) == ord('q'):
        break

tello.streamoff()
tello.land()
cv2.destroyAllWindows()
