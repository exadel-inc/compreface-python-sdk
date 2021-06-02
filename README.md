# CompreFace Python-SDK

CompreFace Python SDK makes face recognition into your application even easier.

## Table of content
  - [Requirements](#requirements)
  - [Usage](#usage)
    - [Initialization](#initialization)
    - [Example Add an Example of a Subject](#example-add-an-example-of-a-subject)
    - [Example Recognize Faces from a Given Image](#example-recognize-faces-from-a-given-image)
    - [Example List of All Saved Subjects](#example-list-of-all-saved-subjects)
    - [Example Delete All Examples of the Subject by Name](#example-delete-all-examples-of-the-subject-by-name)
    - [Example Delete an Example of the Subject by ID](#example-delete-an-example-of-the-subject-by-id)
    - [Example Compare Faces from a Given Image](#example-compare-faces-from-a-given-image)
    - [Example Detect Faces from a Given Image](#example-detect-faces-from-a-given-image)
    - [Example Verify Face from a Given Images](#example-verify-face-from-a-given-images)
  - [Reference](#reference)
    - [Options structure](#options-structure)
    - [Face Recognition Service](#face-recognition-service)
      - [Add an Example of a Subject](#add-an-example-of-a-subject)
      - [Recognize Faces from a Given Image](#recognize-faces-from-a-given-image)
      - [List of All Saved Subjects](#list-of-all-saved-subjects)
      - [Delete All Examples of the Subject by Name](#delete-all-examples-of-the-subject-by-name)
      - [Delete an Example of the Subject by ID](#delete-an-example-of-the-subject-by-id)
      - [Compare Faces from a Given Image](#compare-faces-from-a-given-image)
    - [Face Detection Service](#face-detection-service)
    - [Face Verification Service](#face-verification-service)

## Requirements

Before using our SDK make sure you have installed CompreFace and Python on your machine.

1. [CompreFace](https://github.com/exadel-inc/CompreFace#getting-started-with-compreface)
2. [Python](https://www.python.org/downloads/) (Version 3.7+)

### CompreFace compatibility matrix

| CompreFace Python SDK version | CompreFace 0.4.x | CompreFace 0.5.x |
| --------------------------| ---------------- | ---------------- | 
| 0.1.0                     | ✔                | ✔                | 


## Installation

It can be installed through pip:

```python
$ pip install compreface-sdk
```

## Usage

### Initialization

To start using Python SDK you need to import `CompreFace` object from 'compreface-python-sdk' dependency.  

Then you need to init it with `url` and `port`. By default, if you run CompreFace on your local machine, it's `http://localhost` and `8000` respectively.
You can pass optional `options` object when call method to set default parameters, see reference for [more information](#options-structure).

After you initialized `CompreFace` object you need to init the service object with the `api key` of your face service. You can use this service object to recognize faces.

However, before recognizing you need first to add faces into the face collection. To do this, get the face collection object from the service object.

```python
from compreface import CompreFace
from compreface.service import RecognitionService


DOMAIN: str = 'http://localhost'
PORT: str = '8000'
API_KEY: str = '7dacfc8e-1bb1-4fcf-a9b1-76e4d9d89855'

compre_face: CompreFace = CompreFace(DOMAIN, PORT)

recognition: RecognitionService = compre_face.init_face_recognition(API_KEY)

face_collection: FaceCollection = recognition.get_face_collection()
```

### Example Add an Example of a Subject

**All this examples you can find in repository inside "examples" folder.**

Here is example that shows how to add an image to your face collection from your file system:

```python
face_collection: FaceCollection = recognition.get_face_collection()

image_path: str = 'examples/common/jonathan-petit-unsplash.jpg'
subject: str = 'Jonathan Petit'

face_collection.add(image_path=image_path, subject=subject, options={
    "det_prob_threshold": 0.8
})

```

### Example Recognize Faces from a Given Image

This code snippet shows how to recognize unknown face.

```python
image_path: str or bytes

recognition.recognize(image_path=image_path, options={
    "limit": 0,
    "det_prob_threshold": 0.8,
    "prediction_count": 1,
    "status": "true"
}))


```

### Example List of All Saved Subjects

Here is example to retrieve a list of subjects saved in a Face Collection:

```python
face_collection: FaceCollection = recognition.get_face_collection()

face_collection.list()
```

### Example Delete All Examples of the Subject by Name

Here is example to delete all image examples of the <subject>:

```python
face_collection: FaceCollection = recognition.get_face_collection()

subject: str = 'Jonathan Petit'

print(face_collection.delete_all(subject))

```

### Example Delete an Example of the Subject by ID

This example to delete an image by ID(ID is last and given from server):

```python
face_collection: FaceCollection = recognition.get_face_collection()

faces: list = face_collection.list().get('faces')

if(len(faces) != 0):
    last_face: dict = faces[len(faces) - 1]
    print(face_collection.delete(last_face.get('image_id')))
else:
    print('No subject found')

```

### Example Compare Faces from a Given Image

Here is example to compare faces from the uploaded images with the face in saved image ID:

```python
face_collection: FaceCollection = recognition.get_face_collection()

face: dict = next(item for item in face_collection.list().get('faces') if item['subject'] ==
                  'Jonathan Petit')

image_id = face.get('image_id')

face_collection.verify(image_path=image_path, image_id=image_id, options={
    "limit": 0,
    "det_prob_threshold": 0.8,
    "prediction_count": 1,
    "status": "true"
})
```

### Example Detect Faces from a Given Image

Here is example to detect faces from a given image.

```python
from compreface import CompreFace
from compreface.service import DetectionService

DOMAIN: str = 'http://localhost'
PORT: str = '8000'
DETECTION_API_KEY: str = 'a482a613-3118-4554-a295-153bd6e8ac65'

compre_face: CompreFace = CompreFace(DOMAIN, PORT)

detection: DetectionService = compre_face.init_face_recognition(
    DETECTION_API_KEY)

image_path: str = 'examples/common/jonathan-petit-unsplash.jpg'

detection.detect(image_path=image_path, options={
    "limit": 0,
    "det_prob_threshold": 0.8,
    "prediction_count": 1,
    "face_plugins": "calculator,age,gender,landmarks",
    "status": "true"
})
```

### Example Verify Face from a Given Images
Here is example to verify face from a given images.

```python
from compreface import CompreFace
from compreface.service import VerificationService

DOMAIN: str = 'http://localhost'
PORT: str = '8000'
VERIFICATION_API_KEY: str = '3c6171a4-e115-41f0-afda-4032bda4bfe9'


compre_face: CompreFace = CompreFace(DOMAIN, PORT)

verify: VerificationService = compre_face.init_face_verification(
    VERIFICATION_API_KEY)

image_path: str = 'examples/common/jonathan-petit-unsplash.jpg'


verify.verify(image_path, image_path, {
    "limit": 0,
    "det_prob_threshold": 0.8,
    "prediction_count": 1,
    "face_plugins": "age,gender",
    "status": "true"
})
```

## Reference

## Options structure

**Options is optional field in every request.**

```python 

class DetProbOptionsDict(TypedDict):
    det_prob_threshold: float


class ExpandedOptionsDict(DetProbOptionsDict):
    limit: int
    status: bool
    face_plugins: str


class AllOptionsDict(ExpandedOptionsDict):
    prediction_count: int

```
| Option              | Type    | Notes                                     |
| --------------------| ------  | ----------------------------------------- |
| det_prob_threshold  | string  | minimum required confidence that a recognized face is actually a face. Value is between 0.0 and 1.0 |
| limit               | integer | maximum number of faces on the image to be recognized. It recognizes the biggest faces first. Value of 0 represents no limit. Default value: 0       |
| prediction_count    | integer | maximum number of subject predictions per face. It returns the most similar subjects. Default value: 1    |
| face_plugins        | string  | comma-separated slugs of face plugins. If empty, no additional information is returned. [Learn more](https://github.com/exadel-inc/CompreFace/tree/master/docs/Face-services-and-plugins.md)    |
| status              | boolean | if true includes system information like execution_time and plugin_version fields. Default value is false    |

### Face Recognition Service

### Add an Example of a Subject

This creates an example of the subject by saving images. You can add as many images as you want to train the system.

```python
FaceCollection.add(file, subject, options)
```

| Element            | Description | Type   | Required | Notes                                                                                                |
| ------------------ | ----------- | ------ | -------- | ---------------------------------------------------------------------------------------------------- |
| subject            | param       | string | required | is the name you assign to the image you save                                                         |
| options | param       | string | Object | fields from [Options](#options-structure). Only used here DetProbOptionsDict |
| file               | body        | image  | required | Image can pass from url, local path or bytes. Max size is 5Mb               |

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
| file               | body        | image   | required | Image can pass from url, local path or bytes. Max size is 5Mb                                                         |
| options | param       | string | Object | fields from [Options](#options-structure). All of the OptionsDict are used here  |

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
| age                        | array   | detected age range. Return only if [age plugin](https://github.com/exadel-inc/CompreFace/blob/master/docs/Face-services-and-plugins.md) is enabled                                                       |
| gender                     | string  | detected gender. Return only if [gender plugin](https://github.com/exadel-inc/CompreFace/blob/master/docs/Face-services-and-plugins.md) is enabled                                                       |
| embedding                  | array   | face embeddings. Return only if [calculator plugin](https://github.com/exadel-inc/CompreFace/blob/master/docs/Face-services-and-plugins.md) is enabled                                                   |
| box                        | object  | list of parameters of the bounding box for this face                                                                                                        |
| probability                | float   | probability that a found face is actually a face                                                                                                            |
| x_max, y_max, x_min, y_min | integer | coordinates of the frame containing the face                                                                                                                |
| landmarks                  | array   | list of the coordinates of the frame containing the face-landmarks.|
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

Response body on success:

```
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
| subject   | param       | string | optional | is the name you assign to the image you save. **Caution!** If this parameter is absent, all faces in Face Collection will be removed |

Response body on success:

```
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
| --------- | ----------- | ------ | -------- | ------------------------------------------------------------ 
| image_id  | variable    | UUID   | required | UUID of the removing face                                    |

Response body on success:

```
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
| image_id           | variable    | UUID    | required | UUID of the verifying face                                                                                                                            |
| file               | body        | image   | required | Image can pass from url, local path or bytes. Max size is 5Mb                                                                |
| options | param       | string | Object | fields from [Options](#options-structure). ExpandedOptionsDict or DetProbOptionsDict are used here  |

Response body on success:

```
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

```python
DetectionService.detect(file, options)
```

| Element            | Description | Type    | Required | Notes                                                                                                                                          |
| ------------------ | ----------- | ------- | -------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| image_id           | variable    | UUID    | required | UUID of the verifying face                                                                                                                     |
| file               | body        | image   | required | image where to detect faces. Image can pass from url, local path or bytes. Max size is 5Mb                            |
| options | param       | string | Object | fields from [Options](#options-structure). ExpandedOptionsDict or DetProbOptionsDict are used here  |

Response body on success:

```json
{
  "result": [
    {
      "age": [25, 32],
      "gender": "female",
      "embedding": [-0.03027934394776821, "...", -0.05117142200469971],
      "box": {
        "probability": 0.9987509250640869,
        "x_max": 376,
        "y_max": 479,
        "x_min": 68,
        "y_min": 77
      },
      "landmarks": [
        [156, 245],
        [277, 253],
        [202, 311],
        [148, 358],
        [274, 365]
      ],
      "execution_time": {
        "age": 30.0,
        "gender": 26.0,
        "detector": 130.0,
        "calculator": 49.0
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

## Face Verification Service

To compare faces from given two images:

```python
VerificationService.verify(source_image, target_image, options)
```

| Element            | Description | Type    | Required | Notes                                                                                                                                                 |
| ------------------ | ----------- | ------- | -------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| image_id           | variable    | UUID    | required | UUID of the verifying face                                                                                                                            |
| source_image       | body        | image   | required | file to be verified. Image can pass from url, local path or bytes. Max size is 5Mb                                           |
| target_image       | body        | image   | required | reference file to check the source file. Image can pass from url, local path or bytes. Max size is 5Mb                       |
| options | param       | string | Object | fields from [Options](#options-structure). ExpandedOptionsDict or DetProbOptionsDict are used here  |                                          

Response body on success:

```json
{
  "source_image_face" : {
    "age" : [ 25, 32 ],
    "gender" : "female",
    "embedding" : [ -0.0010271212086081505, "...", -0.008746841922402382 ],
    "box" : {
      "probability" : 0.9997453093528748,
      "x_max" : 205,
      "y_max" : 167,
      "x_min" : 48,
      "y_min" : 0
    },
    "landmarks" : [ [ 92, 44 ], [ 130, 68 ], [ 71, 76 ], [ 60, 104 ], [ 95, 125 ] ],
    "execution_time" : {},
  "face_matches": [
    {
      "age" : [ 25, 32 ],
      "gender" : "female",
      "embedding" : [ -0.049007344990968704, "...", -0.01753818802535534 ],
      "box" : {
        "probability" : 0.99975,
        "x_max" : 308,
        "y_max" : 180,
        "x_min" : 235,
        "y_min" : 98
      },
      "landmarks" : [ [ 260, 129 ], [ 273, 127 ], [ 258, 136 ], [ 257, 150 ], [ 269, 148 ] ],
      "similarity" : 0.97858,
      "execution_time" : {
        "age" : 59.0,
        "gender" : 30.0,
        "detector" : 177.0,
        "calculator" : 70.0
      }
    }],
  "plugins_versions" : {
    "age" : "agegender.AgeDetector",
    "gender" : "agegender.GenderDetector",
    "detector" : "facenet.FaceDetector",
    "calculator" : "facenet.Calculator"
  }
}
```

| Element                    | Type    | Description                                                                        |
| -------------------------- | ------- | ---------------------------------------------------------------------------------- |
| source_image_face          | object  | additional info about source image face                                            |
| face_matches               | array   | result of face verification                                                        |
| age                        | array   | detected age range.                                                                |
| gender                     | string  | detected gender. Return only if                                                    |
| embedding                  | array   | face embeddings. Return only if                                                    |
| box                        | object  | list of parameters of the bounding box for this face                               |
| probability                | float   | probability that a found face is actually a face                                   |
| x_max, y_max, x_min, y_min | integer | coordinates of the frame containing the face                                       |
| landmarks                  | array   | list of the coordinates of the frame containing the face-landmarks. Return only if |
| similarity                 | float   | similarity between this face and the face on the source image                      |
| execution_time             | object  | execution time of all plugins                                                      |
| plugins_versions           | object  | contains information about plugin versions                                         |
