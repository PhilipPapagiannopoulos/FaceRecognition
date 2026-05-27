import cv2
from datetime import datetime

face_classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)
recolor = (0,0,0)

def detect_bouncing_box(vid):
    mitsos = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #mitsos = cv2.flip(mitsos, 1)
    faces = face_classifier.detectMultiScale(mitsos, 1.1, 5, minSize=(40, 40))
    #print("Faces: ", len(faces)) #---------- len=length and faces = list

    for(x, y, w, h) in faces:
        cv2.rectangle(vid, (x,y), (x+w, y+h), recolor, 2 ) #recolor=(255,0,0)
    return faces

while True:
    ok, frame = cap.read()
    if not ok:
        break

    faces = detect_bouncing_box(frame)
    face_count= len(faces)
    cv2.putText(frame, f"Faces: {face_count}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    cv2.imshow("Webcam", frame)



    key = cv2.waitKey(1)
    if  key % 256 == 27: #esc button
        break
    elif key % 256 == ord('b'):
        recolor = (255,0,0)
    elif key % 256 == ord('g'):
        recolor = (0,225,0)
    elif key % 256 == ord('r'):
        recolor = (0,0,255)
    elif key % 256 == ord(' '): #or I could use ...256 == 32
        now = datetime.now()
        imgName = "Frame at time" + str(now.hour) + "." + str(now.minute) + "." + str(now.second) + ".png"
        cv2.imwrite(imgName, frame)
        print("Image saved: ", imgName)


cap.release()
cv2.destroyAllWindows()
