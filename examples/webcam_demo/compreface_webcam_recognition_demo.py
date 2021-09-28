import cv2
from compreface import CompreFace
from compreface.service import RecognitionService

DOMAIN: str = 'http://localhost'
PORT: str = '8000'
RECOGNITION_API_KEY: str = 'RECOGNITION_API_KEY'


compre_face: CompreFace = CompreFace(DOMAIN, PORT, {
    "limit": 0,
    "det_prob_threshold": 0.8,
    "prediction_count": 1,
    "face_plugins": "age,gender,landmarks,mask",
    "status": False
})

recognition: RecognitionService = compre_face.init_face_recognition(RECOGNITION_API_KEY)

cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()

    if not ret:
        break

    frame = cv2.flip(frame, 1)
    _, im_buf_arr = cv2.imencode(".jpg", frame)
    byte_im = im_buf_arr.tobytes()
    data = recognition.recognize(byte_im)
    results = data.get('result')
    if results:
        for result in results:
            box = result.get('box')
            age = result.get('age')
            gender = result.get('gender')
            mask = result.get('mask')
            subjects = result.get('subjects')
            if box and age and gender and mask:
                age = f"Age: {age['low']} - {age['high']}"
                gender = f"Gender: {gender['value']}"
                mask = f"Mask: {mask['value']}"
                cv2.rectangle(img=frame, pt1=(box['x_min'], box['y_min']),
                              pt2=(box['x_max'], box['y_max']), color=(0, 255, 0), thickness=1)
                cv2.putText(frame, age, (box['x_max'], box['y_min'] + 15),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 1)
                cv2.putText(frame, gender, (box['x_max'], box['y_min'] + 35),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 1)
                cv2.putText(frame, mask, (box['x_max'], box['y_min'] + 55),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 1)

                if subjects:
                    subjects = sorted(subjects, key=lambda k: k['similarity'], reverse=True)
                    subject = f"Subject: {subjects[0]['subject']}"
                    similarity = f"Similarity: {subjects[0]['similarity']}"
                    cv2.putText(frame, subject, (box['x_max'], box['y_min'] + 75),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 1)
                    cv2.putText(frame, similarity, (box['x_max'], box['y_min'] + 95),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 1)
                else:
                    subject = f"Subject: Not recognized"
                    cv2.putText(frame, subject, (box['x_max'], box['y_min'] + 75),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 1)

        cv2.imshow('CompreFace demo', frame)
    else:
        print(data)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
