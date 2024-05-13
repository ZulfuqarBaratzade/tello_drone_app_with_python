import cv2
import djitellopy
tello = djitellopy.Tello()



tello.connect()
tello.streamon()
frame_read = tello.get_frame_read()
cv2.namedWindow('Tello Video')
tello.get_battery()

tello.takeoff()
tello.move_forward(50)
tello.rotate_clockwise(180)

while True:
    frame = frame_read.frame
    cv2.imshow('Tello Video', frame)
    
    if cv2.waitKey(1) == ord('q'):
        break
tello.streamoff()
tello.land()

# dron = Tello()
# dron.connect()
# 


# dron.takeoff()

# dron.move_forward(10)
# dron.
# dron.move_forward(10)


# dron.land()


# print(dir(djitellopy))
# import cv2

# while True:
#     frame = djitellopy.tello.get_frame_read().frame
#     cv2.imshow("Tello Video", frame)

#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# cv2.destroyAllWindows()
