# CompreFace Python-SDK

CompreFace is free and open-source face recognition system from Exadel and this Python SDK helps you to use all functionalities of the system in your application without prior skills.

## Content

- [Installation](#installation)
- [Recognition Service](#recognition)
- [Usage](#usage)

## Rest API description

By using the created API key, the user can add an image as an example of a particular face, retrieve a list of saved images, recognize a face from the image uploaded to the Face Collection, and delete all examples of the face by the name.

## Requirements

Before using our SDK make sure you have installed CompreFace and Python on your machine.

1. [CompreFace](https://github.com/exadel-inc/CompreFace#getting-started-with-compreface)
2. [Python](https://nodejs.org/en/) (Version 3.7)
3. [requests-toolbelt] (pip install requests-toolbelt==0.9.1)

## Recognition Service

### Add an Example of a Subject

This creates an example of the subject by saving images. You can add as many images as you want to train the system.

```python
FaceCollection.add(file, subject)
```

| Element            | Description | Type   | Required | Notes                                                                                                |
| ------------------ | ----------- | ------ | -------- | ---------------------------------------------------------------------------------------------------- |
| Content-Type       | header      | string | required | multipart/form-data                                                                                  |
| x-api-key          | header      | string | required | api key of the Face recognition service, created by the user                                         |
| subject            | param       | string | required | is the name you assign to the image you save                                                         |
| det_prob_threshold | param       | string | optional | minimum required confidence that a recognized face is actually a face. Value is between 0.0 and 1.0. |
| file               | body        | image  | required | allowed image formats: jpeg, jpg, ico, png, bmp, gif, tif, tiff, webp. Max size is 5Mb               |

Response body on success:

```json
{
  "image_id": "6b135f5b-a365-4522-b1f1-4c9ac2dd0728",
  "subject": "subject1"
}
```

| Element  | Type   | Description                |
| -------- | ------ | -------------------------- |
| image_id | UUID   | UUID of uploaded image     |
| subject  | string | Subject of the saved image |

### Recognize Faces from a Given Image

Recognizes faces from the uploaded image.

```python
RecognitionService.recognize(file, options)
```

| Element            | Description | Type    | Required | Notes                                                                                                                                          |
| ------------------ | ----------- | ------- | -------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| Content-Type       | header      | string  | required | multipart/form-data                                                                                                                            |
| x-api-key          | header      | string  | required | api key of the Face recognition service, created by the user                                                                                   |
| file               | body        | image   | required | allowed image formats: jpeg, jpg, ico, png, bmp, gif, tif, tiff, webp. Max size is 5Mb                                                         |
| limit              | param       | integer | optional | maximum number of faces on the image to be recognized. It recognizes the biggest faces first. Value of 0 represents no limit. Default value: 0 |
| det_prob_threshold | param       | string  | optional | minimum required confidence that a recognized face is actually a face. Value is between 0.0 and 1.0.                                           |
| prediction_count   | param       | integer | optional | maximum number of subject predictions per face. It returns the most similar subjects. Default value: 1                                         |
| face_plugins       | param       | string  | optional | comma-separated slugs of face plugins. If empty, no additional information is returned. [Learn more](Face-services-and-plugins.md)             |
| status             | param       | boolean | optional | if true includes system information like execution_time and plugin_version fields. Default value is false                                      |

Response body on success:

```json
{
  "result": [
    {
      "age": [25, 32],
      "gender": "female",
      "embedding": [9.424854069948196e-4, "...", -0.011415496468544006],
      "box": {
        "probability": 1.0,
        "x_max": 1420,
        "y_max": 1368,
        "x_min": 548,
        "y_min": 295
      },
      "landmarks": [
        [814, 713],
        [1104, 829],
        [832, 937],
        [704, 1030],
        [1017, 1133]
      ],
      "subjects": [
        {
          "similarity": 0.97858,
          "subject": "subject1"
        }
      ],
      "execution_time": {
        "age": 28.0,
        "gender": 26.0,
        "detector": 117.0,
        "calculator": 45.0
      }
    }
  ],
  "plugins_versions": {
    "age": "agegender.AgeDetector",
    "gender": "agegender.GenderDetector",
    "detector": "facenet.FaceDetector",
    "calculator": "facenet.Calculator"
  }
}
```

| Element                    | Type    | Description                                                                                                                                                 |
| -------------------------- | ------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| age                        | array   | detected age range. Return only if [age plugin](Face-services-and-plugins.md#face-plugins) is enabled                                                       |
| gender                     | string  | detected gender. Return only if [gender plugin](Face-services-and-plugins.md#face-plugins) is enabled                                                       |
| embedding                  | array   | face embeddings. Return only if [calculator plugin](Face-services-and-plugins.md#face-plugins) is enabled                                                   |
| box                        | object  | list of parameters of the bounding box for this face                                                                                                        |
| probability                | float   | probability that a found face is actually a face                                                                                                            |
| x_max, y_max, x_min, y_min | integer | coordinates of the frame containing the face                                                                                                                |
| landmarks                  | array   | list of the coordinates of the frame containing the face-landmarks. Return only if [landmarks plugin](Face-services-and-plugins.md#face-plugins) is enabled |
| subjects                   | list    | list of similar subjects with size of <prediction_count> order by similarity                                                                                |
| similarity                 | float   | similarity that on that image predicted person                                                                                                              |
| subject                    | string  | name of the subject in Face Collection                                                                                                                      |
| execution_time             | object  | execution time of all plugins                                                                                                                               |
| plugins_versions           | object  | contains information about plugin versions                                                                                                                  |

### List of All Saved Subjects

To retrieve a list of subjects saved in a Face Collection:

```python
FaceCollection.list()
```

| Element   | Description | Type   | Required | Notes                                                        |
| --------- | ----------- | ------ | -------- | ------------------------------------------------------------ |
| x-api-key | header      | string | required | api key of the Face recognition service, created by the user |

Response body on success:

```json
{
  "faces": [
    {
      "image_id": <image_id>,
      "subject": <subject>
    },
    ...
  ]
}
```

| Element  | Type   | Description                                                       |
| -------- | ------ | ----------------------------------------------------------------- |
| image_id | UUID   | UUID of the face                                                  |
| subject  | string | <subject> of the person, whose picture was saved for this api key |

### Delete All Examples of the Subject by Name

To delete all image examples of the <subject>:

```python
FaceCollection.delete_all(subject)
```

| Element   | Description | Type   | Required | Notes                                                                                                                                |
| --------- | ----------- | ------ | -------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| x-api-key | header      | string | required | api key of the Face recognition service, created by the user                                                                         |
| subject   | param       | string | optional | is the name you assign to the image you save. **Caution!** If this parameter is absent, all faces in Face Collection will be removed |

Response body on success:

```json
[
  {
    "image_id": <image_id>,
    "subject": <subject>
  },
  ...
]
```

| Element  | Type   | Description                                                       |
| -------- | ------ | ----------------------------------------------------------------- |
| image_id | UUID   | UUID of the removed face                                          |
| subject  | string | <subject> of the person, whose picture was saved for this api key |

### Delete an Example of the Subject by ID

To delete an image by ID:

```python
FaceCollection.delete(image_id)
```

| Element   | Description | Type   | Required | Notes                                                        |
| --------- | ----------- | ------ | -------- | ------------------------------------------------------------ |
| x-api-key | header      | string | required | api key of the Face recognition service, created by the user |
| image_id  | variable    | UUID   | required | UUID of the removing face                                    |

Response body on success:

```json
{
  "image_id": <image_id>,
  "subject": <subject>
}
```

| Element  | Type   | Description                                                       |
| -------- | ------ | ----------------------------------------------------------------- |
| image_id | UUID   | UUID of the removed face                                          |
| subject  | string | <subject> of the person, whose picture was saved for this api key |

### Verify Faces from a Given Image

To compare faces from the uploaded images with the face in saved image ID:

```python
FaceCollection.verify(image_id, file, options)
```

| Element            | Description | Type    | Required | Notes                                                                                                                                                 |
| ------------------ | ----------- | ------- | -------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| Content-Type       | header      | string  | required | multipart/form-data                                                                                                                                   |
| x-api-key          | header      | string  | required | api key of the Face recognition service, created by the user                                                                                          |
| image_id           | variable    | UUID    | required | UUID of the verifying face                                                                                                                            |
| file               | body        | image   | required | allowed image formats: jpeg, jpg, ico, png, bmp, gif, tif, tiff, webp. Max size is 5Mb                                                                |
| limit              | param       | integer | optional | maximum number of faces on the target image to be recognized. It recognizes the biggest faces first. Value of 0 represents no limit. Default value: 0 |
| det_prob_threshold | param       | string  | optional | minimum required confidence that a recognized face is actually a face. Value is between 0.0 and 1.0.                                                  |
| face_plugins       | param       | string  | optional | comma-separated slugs of face plugins. If empty, no additional information is returned. [Learn more](Face-services-and-plugins.md)                    |
| status             | param       | boolean | optional | if true includes system information like execution_time and plugin_version fields. Default value is false                                             |

Response body on success:

```json
{
  "result": [
    {
      "box": {
        "probability": <probability>,
        "x_max": <integer>,
        "y_max": <integer>,
        "x_min": <integer>,
        "y_min": <integer>
      },
      "similarity": <similarity1>
    },
    ...
  ]
}
```

| Element                    | Type    | Description                                          |
| -------------------------- | ------- | ---------------------------------------------------- |
| box                        | object  | list of parameters of the bounding box for this face |
| probability                | float   | probability that a found face is actually a face     |
| x_max, y_max, x_min, y_min | integer | coordinates of the frame containing the face         |
| similarity                 | float   | similarity that on that image predicted person       |
| subject                    | string  | name of the subject in Face Collection               |

## Face Detection Service

To detect faces from the uploaded image:

| Element            | Description | Type    | Required | Notes                                                                                                                                          |
| ------------------ | ----------- | ------- | -------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| Content-Type       | header      | string  | required | multipart/form-data                                                                                                                            |
| x-api-key          | header      | string  | required | api key of the Face Detection service, created by the user                                                                                     |
| image_id           | variable    | UUID    | required | UUID of the verifying face                                                                                                                     |
| file               | body        | image   | required | image where to detect faces. Allowed image formats: jpeg, jpg, ico, png, bmp, gif, tif, tiff, webp. Max size is 5Mb                            |
| limit              | param       | integer | optional | maximum number of faces on the image to be recognized. It recognizes the biggest faces first. Value of 0 represents no limit. Default value: 0 |
| det_prob_threshold | param       | string  | optional | minimum required confidence that a recognized face is actually a face. Value is between 0.0 and 1.0                                            |
| face_plugins       | param       | string  | optional | comma-separated slugs of face plugins. If empty, no additional information is returned. [Learn more](Face-services-and-plugins.md)             |
| status             | param       | boolean | optional | if true includes system information like execution_time and plugin_version fields. Default value is false                                      |

Response body on success:

````json
{
  "result" : [ {
    "age" : [ 25, 32 ],
    "gender" : "female",
    "embedding" : [ -0.03027934394776821, "...", -0.05117142200469971 ],
    "box" : {
      "probability" : 0.9987509250640869,
      "x_max" : 376,
      "y_max" : 479,
      "x_min" : 68,
      "y_min" : 77
    },
    "landmarks" : [ [ 156, 245 ], [ 277, 253 ], [ 202, 311 ], [ 148, 358 ], [ 274, 365 ] ],
    "execution_time" : {
      "age" : 30.0,
      "gender" : 26.0,
      "detector" : 130.0,
      "calculator" : 49.0
    }
  } ],
  "plugins_versions" : {
    "age" : "agegender.AgeDetector",
    "gender" : "agegender.GenderDetector",
    "detector" : "facenet.FaceDetector",
    "calculator" : "facenet.Calculator"
  }
}
```                                    |

## Usage

You only need to import and initialize CompreFace in order to use functionalities of services. Below given initial setup recognition service for your application.

```python
from compreface import CompreFace
from compreface.service import RecognitionService


DOMAIN: str = 'http://localhost'
PORT: str = '8000'
API_KEY: str = '7dacfc8e-1bb1-4fcf-a9b1-76e4d9d89855'

compre_face: CompreFace = CompreFace(DOMAIN, PORT)

recognition: RecognitionService = compre_face.init_face_recognition(API_KEY)
````

### Example Add an Example of a Subject

This creates an example of the subject by saving images. You can add as many images as you want to train the system.

```python
# -*- coding: utf-8 -*-

from compreface import CompreFace
from compreface.service import RecognitionService
from compreface.collections import FaceCollection

DOMAIN: str = 'http://localhost'
PORT: str = '8000'
RECOGNITION_API_KEY: str = '9916f5d1-216f-4049-9e06-51c140bfa898'

compre_face: CompreFace = CompreFace(DOMAIN, PORT)

recognition: RecognitionService = compre_face.init_face_recognition(
    RECOGNITION_API_KEY)

face_collection: FaceCollection = recognition.get_face_collection()

image_path: str = 'examples/common/di_kaprio.jpg'
subject: str = 'Leonardo Wilhelm DiCaprio'

print(face_collection.add(image_path=image_path, subject=subject, options={
    "det_prob_threshold": 0.8
}))

```

### Example Recognize Faces from a Given Image

Recognizes faces from the uploaded image.

```python
# -*- coding: utf-8 -*-

from compreface import CompreFace
from compreface.service import RecognitionService

DOMAIN: str = 'http://localhost'
PORT: str = '8000'
RECOGNITION_API_KEY: str = '9916f5d1-216f-4049-9e06-51c140bfa898'


compre_face: CompreFace = CompreFace(DOMAIN, PORT)

recognition: RecognitionService = compre_face.init_face_recognition(
    RECOGNITION_API_KEY)

image_path: str = 'examples/common/di_kaprio.jpg'

print(recognition.recognize(image_path=image_path, options={
    "limit": 0,
    "det_prob_threshold": 0.8,
    "prediction_count": 1,
    "status": "true"
}))


```

### Example List of All Saved Subjects

To retrieve a list of subjects saved in a Face Collection:

```python
# -*- coding: utf-8 -*-

from compreface import CompreFace
from compreface.service import RecognitionService
from compreface.collections import FaceCollection

DOMAIN: str = 'http://localhost'
PORT: str = '8000'
RECOGNITION_API_KEY: str = '9916f5d1-216f-4049-9e06-51c140bfa898'


compre_face: CompreFace = CompreFace(DOMAIN, PORT)

recognition: RecognitionService = compre_face.init_face_recognition(
    RECOGNITION_API_KEY)

face_collection: FaceCollection = recognition.get_face_collection()

print(face_collection.list())

```

### Example Delete All Examples of the Subject by Name

To delete all image examples of the <subject>:

```python
# -*- coding: utf-8 -*-

from compreface import CompreFace
from compreface.service import RecognitionService
from compreface.collections import FaceCollection

DOMAIN: str = 'http://localhost'
PORT: str = '8000'
RECOGNITION_API_KEY: str = '9916f5d1-216f-4049-9e06-51c140bfa898'


compre_face: CompreFace = CompreFace(DOMAIN, PORT)

recognition: RecognitionService = compre_face.init_face_recognition(
    RECOGNITION_API_KEY)
subject: str = 'Leonardo Wilhelm DiCaprio'

face_collection: FaceCollection = recognition.get_face_collection()

print(face_collection.delete_all(subject))

```

### Example Delete an Example of the Subject by ID(ID is last and given from server)

To delete an image by ID:

```python
from compreface import CompreFace
from compreface.service import RecognitionService
from compreface.collections import FaceCollection

DOMAIN: str = 'http://localhost'
PORT: str = '8000'
RECOGNITION_API_KEY: str = '9916f5d1-216f-4049-9e06-51c140bfa898'


compre_face: CompreFace = CompreFace(DOMAIN, PORT)

recognition: RecognitionService = compre_face.init_face_recognition(
    RECOGNITION_API_KEY)

face_collection: FaceCollection = recognition.get_face_collection()

faces: list = face_collection.list().get('faces')

if(len(faces) != 0):
    last_face: dict = faces[len(faces) - 1]
    print(face_collection.delete(last_face.get('image_id')))
else:
    print('No subject found')

```

### Example Verify Faces from a Given Image

To compare faces from the uploaded images with the face in saved image ID:

```python
from compreface.collections.face_collections import FaceCollection
from compreface import CompreFace
from compreface.service import RecognitionService

DOMAIN: str = 'http://localhost'
PORT: str = '8000'
RECOGNITION_API_KEY: str = '9916f5d1-216f-4049-9e06-51c140bfa898'

compre_face: CompreFace = CompreFace(DOMAIN, PORT)

recognition: RecognitionService = compre_face.init_face_recognition(
    RECOGNITION_API_KEY)

image_path: str = 'examples/common/di_kaprio.jpg'

face_collection: FaceCollection = recognition.get_face_collection()

face: dict = next(item for item in face_collection.list().get('faces') if item['subject'] ==
                  'Leonardo Wilhelm DiCaprio')

image_id = face.get('image_id')

print(face_collection.verify(image_path=image_path, image_id=image_id, options={
    "limit": 0,
    "det_prob_threshold": 0.8,
    "prediction_count": 1,
    "status": "true"
}))
```

### Example Detect Faces from a Given Image

```python

from compreface.collections.face_collections import FaceCollection
from compreface import CompreFace
from compreface.service import DetectionService


DOMAIN: str = 'http://localhost'
PORT: str = '8000'
DETECTION_API_KEY: str = 'a482a613-3118-4554-a295-153bd6e8ac65'

compre_face: CompreFace = CompreFace(DOMAIN, PORT)

detection: DetectionService = compre_face.init_face_recognition(
    DETECTION_API_KEY)

image_path: str = 'examples/common/di_kaprio.jpg'

face_collection: FaceCollection = detection.get_face_collection()

print(face_collection.detect(image_path=image_path, options={
    "limit": 0,
    "det_prob_threshold": 0.8,
    "prediction_count": 1,
    "face_plugins": "calculator,age,gender,landmarks",
    "status": "true"
}))
```

options is optional field.

All this examples you can find in repozitory inside "examples" folder.
