# Webcam demo

This is an example of how to use CompreFace face recognition with python sdk.

# Requirements

1. [Python](https://www.python.org/downloads/) (Version 3.7+)
2. [CompreFace](https://github.com/exadel-inc/CompreFace#getting-started-with-compreface)
3. [Compreface-python-sdk](https://github.com/exadel-inc/compreface-python-sdk)
4. [Opencv-python](https://pypi.org/project/opencv-python/)

# Face recognition demo

To run the demo, open `webcam_demo` folder and run:

```commandline
python compreface_webcam_recognition_demo.py --api-key your_api_key --host http://localhost --port 8000
```
* `--api-key` is your Face Recognition service API key. API key for this demo was created on step 5 of [How to Use CompreFace](https://github.com/exadel-inc/CompreFace/blob/master/docs/How-to-Use-CompreFace.md#how-to-use-compreface). Optional value. By default, the value is `00000000-0000-0000-0000-000000000002` - api key with celebrities demo.
* `--host` is the host where you deployed CompreFace. Optional value. By default, the value is `http://localhost`
* `--port` is the port of CompreFace instance. Optional value. By default, the value is `8000`

# Face detection demo

To run the demo, open `webcam_demo` folder and run:

```commandline
python compreface_webcam_detection_demo.py --api-key your_api_key --host http://localhost --port 8000
```
* `--api-key` is your Face Detection service API key. API key for this demo was created on step 5 of [How to Use CompreFace](https://github.com/exadel-inc/CompreFace/blob/master/docs/How-to-Use-CompreFace.md#how-to-use-compreface).
* `--host` is the host where you deployed CompreFace. Optional value. By default, the value is `http://localhost`
* `--port` is the port of CompreFace instance. Optional value. By default, the value is `8000`