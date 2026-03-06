import face_recognition
import cv2
import os

def recognize_face():

    cam = cv2.VideoCapture(0)

    while True:

        ret, frame = cam.read()

        if not ret:
            break

        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        face_locations = face_recognition.face_locations(rgb)

        if len(face_locations) == 0:

            cv2.imshow("Login Camera", frame)

            if cv2.waitKey(1) == ord("q"):
                break

            continue

        face_encodings = face_recognition.face_encodings(rgb, face_locations)

        login_encoding = face_encodings[0]

        for file in os.listdir("faces"):

            if file.endswith(".jpg"):

                image = face_recognition.load_image_file(f"faces/{file}")

                encodings = face_recognition.face_encodings(image)

                if len(encodings) == 0:
                    continue

                saved_encoding = encodings[0]

                distance = face_recognition.face_distance([saved_encoding], login_encoding)

                print("Checking:", file)
                print("Distance:", distance)

                if distance[0] < 0.65:

                    cam.release()
                    cv2.destroyAllWindows()

                    return file.split(".")[0]

        cv2.imshow("Login Camera", frame)

        if cv2.waitKey(1) == ord("q"):
            break

    cam.release()
    cv2.destroyAllWindows()

    return None