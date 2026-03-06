import cv2
import os

def capture_face(name):

    if not os.path.exists("faces"):
        os.makedirs("faces")

    cam = cv2.VideoCapture(0)

    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    )

    print("Press S to capture face")

    while True:

        ret, frame = cam.read()

        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        face_img = None

        for (x, y, w, h) in faces:

            face_img = frame[y:y+h, x:x+w]

            cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 2)

        cv2.imshow("Capture Face", frame)

        key = cv2.waitKey(1)

        if key == ord("s") and face_img is not None:

            face_img = cv2.resize(face_img,(200,200))

            cv2.imwrite(f"faces/{name}.jpg", face_img)

            print("Face saved!")

            break

        if key == ord("q"):
            break

    cam.release()
    cv2.destroyAllWindows()