import cv2 as cv

cap = cv.VideoCapture(0)

eye_cascade = cv.CascadeClassifier('haarcascade_eye.xml')
face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')

# img = cv.imread('face.jpg')

while True:
    ret, frame = cap.read()
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    print(len(faces))

    for(x, y, w, h) in faces:
        cv.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        face_gray = gray[y:y + h, x:x + w]
        face_color = frame[y:y + h, x:x + w]
        eyes = eye_cascade.detectMultiScale(face_gray)
        for (ex, ey, ew, eh) in eyes:
            cv.rectangle(face_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

    cv.imshow('frame', frame)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cv.destroyAllWindows()
