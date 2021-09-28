# Webcam demo

This is an example of how to use CompreFace detection service with python sdk.

## Requirements

1. [Python](https://www.python.org/downloads/) (Version 3.7+)
2. [CompreFace](https://github.com/exadel-inc/CompreFace#getting-started-with-compreface)
3. [Compreface-python-sdk](https://github.com/exadel-inc/compreface-python-sdk)
4. [Opencv-python](https://pypi.org/project/opencv-python/)

## Usage

1. Let's start with setting up our sdk.
```python
from compreface import CompreFace
from compreface.service import DetectionService

DOMAIN: str = 'http://localhost'
PORT: str = '8000'
API_KEY: str = 'your_face_detection_key'

compre_face: CompreFace = CompreFace(DOMAIN, PORT)

detection: DetectionService = compre_face.init_face_detection(API_KEY)
```
2. Then we have to start our webcam, get one frame, convert it to the byte array.
```python
import cv2

cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()

    frame = cv2.flip(frame, 1)
    _, im_buf_arr = cv2.imencode(".jpg", frame)
    byte_im = im_buf_arr.tobytes()
    
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
```
3. Process image with compreface detection service.
```python
data = detection.detect(byte_im)
```
4. Draw an image on our video stream with additional info.
```python
cv2.rectangle(img=frame, pt1=(x_min, y_min), pt2=(x_max, y_max), color=(0, 255, 0), thickness=1)
cv2.putText(frame, age, (x_max, y_min + 15), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 1)
cv2.imshow('CompreFace webcam demo', frame)
```
5. Final code should look like this.
```python
import cv2
from compreface import CompreFace
from compreface.service import DetectionService


DOMAIN: str = 'http://localhost'
PORT: str = '8000'
DETECTION_API_KEY: str = 'detection_api_key'

compre_face: CompreFace = CompreFace(DOMAIN, PORT, {
    "limit": 0,
    "det_prob_threshold": 0.8,
    "prediction_count": 1,
    "face_plugins": "age,gender,landmarks,mask",
    "status": True
})

detection: DetectionService = compre_face.init_face_detection(DETECTION_API_KEY)

cap = cv2.VideoCapture(0)

while cap.isOpened():
    success, frame = cap.read()

    if not success:
        break

    frame = cv2.flip(frame, 1) 
    _, im_buf_arr = cv2.imencode(".jpg", frame)
    byte_im = im_buf_arr.tobytes()
    data = detection.detect(byte_im)
    results = data.get('result')
    if results:
        for result in results:
            box = result.get('box')
            age = result.get('age')
            gender = result.get('gender')
            mask = result.get('mask')
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

        cv2.imshow('CompreFace demo', frame)

    if cv2.waitKey(1) & 0xFF == 27: # Close window with esc button
        break

cap.release()
cv2.destroyAllWindows()
```
6. Run demo
```bash
python compreface_webcam_demo.py
```