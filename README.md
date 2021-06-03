# CompreFace Python SDK

CompreFace Python SDK makes face recognition into your application even easier.

## Table of content
- [Requirements](#requirements)
- [Installation](#installation)
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
    - [CompreFace Global Object](#compreFace-global-object)
    - [Options structure](#options-structure)
    - [Face Recognition Service](#face-recognition-service)
      - [Add an Example of a Subject](#add-an-example-of-a-subject)
      - [Recognize Faces from a Given Image](#recognize-faces-from-a-given-image)
      - [List of All Saved Subjects](#list-of-all-saved-subjects)
      - [Delete All Examples of the Subject by Name](#delete-all-examples-of-the-subject-by-name)
      - [Delete an Example of the Subject by ID](#delete-an-example-of-the-subject-by-id)
      - [Verify Faces from a Given Image](#verify-faces-from-a-given-image)
    - [Face Detection Service](#face-detection-service)
    - [Face Verification Service](#face-verification-service)

## Requirements

Before using our SDK make sure you have installed CompreFace and Python on your machine.

1. [CompreFace](https://github.com/exadel-inc/CompreFace#getting-started-with-compreface)
2. [Python](https://www.python.org/downloads/) (Version 3.7+)

### CompreFace compatibility matrix

| CompreFace Python SDK version | CompreFace 0.5.x |
| ------------------------------| ---------------- | 
| 0.1.0                         | ✔                | 


## Installation

It can be installed through pip:

```shell
pip install compreface-sdk
```

## Usage

All these examples you can find in repository inside [examples](/examples) folder.

### Initialization

To start using Python SDK you need to import `CompreFace` object from 'compreface-sdk' dependency.  

Then you need to init it with `url` and `port`. By default, if you run CompreFace on your local machine, it's `http://localhost` and `8000` respectively.
You can pass optional `options` object when call method to set default parameters, see reference for [more information](#options-structure).

After you initialized `CompreFace` object you need to init the service object with the `api key` of your face service. You can use this service object to recognize faces.

However, before recognizing you need first to add faces into the face collection. To do this, get the face collection object from the service object.

```python
from compreface import CompreFace
from compreface.service import RecognitionService
from compreface.collections import FaceCollection

DOMAIN: str = 'http://localhost'
PORT: str = '8000'
API_KEY: str = 'your_face_recognition_key'

compre_face: CompreFace = CompreFace(DOMAIN, PORT)

recognition: RecognitionService = compre_face.init_face_recognition(API_KEY)

face_collection: FaceCollection = recognition.get_face_collection()
```

### Example. Add an Example of a Subject

Here is example that shows how to add an image to your face collection from your file system:

```python
image_path: str = 'examples/common/jonathan-petit-unsplash.jpg'
subject: str = 'Jonathan Petit'

face_collection.add(image_path=image_path, subject=subject)
```

### Example. Recognize Faces from a Given Image

This code snippet shows how to recognize unknown face.

```python
image_path: "str or bytes"

recognition.recognize(image_path=image_path)
```

### Example. List of All Saved Subjects

This code shows how to retrieve a list of subject examples saved in a Face Collection:

```python
face_collection.list()
```

### Example. Delete All Examples of the Subject by Name

This code shows how to delete all image examples of the subject:

```python
subject: str = 'Jonathan Petit'

print(face_collection.delete_all(subject))

```

### Example. Delete an Example of the Subject by ID

This example to delete an image by ID:

```python
faces: list = face_collection.list().get('faces')

if(len(faces) != 0):
    last_face: dict = faces[len(faces) - 1]
    print(face_collection.delete(last_face.get('image_id')))
else:
    print('No subject found')

```

### Example. Compare Faces from a Given Image

This example shows how to compare unknown face with existing face in face collection:

```python
image_path: "str or bytes"

face: dict = next(item for item in face_collection.list().get('faces') if item['subject'] ==
                  'Jonathan Petit')

image_id = face.get('image_id')

face_collection.verify(image_path=image_path, image_id=image_id)
```

### Example. Detect Faces from a Given Image

Here is example to detect faces from a given image.

```python
from compreface import CompreFace
from compreface.service import DetectionService

DOMAIN: str = 'http://localhost'
PORT: str = '8000'
DETECTION_API_KEY: str = 'your_face_detection_key'

compre_face: CompreFace = CompreFace(DOMAIN, PORT)

detection: DetectionService = compre_face.init_face_detection(DETECTION_API_KEY)

image_path: str = 'examples/common/jonathan-petit-unsplash.jpg'

detection.detect(image_path=image_path)
```

### Example. Verify Face from a Given Images
Here is example to verify face from a given images.

```python
from compreface import CompreFace
from compreface.service import VerificationService

DOMAIN: str = 'http://localhost'
PORT: str = '8000'
VERIFICATION_API_KEY: str = 'your_face_verification_key'

compre_face: CompreFace = CompreFace(DOMAIN, PORT)

verify: VerificationService = compre_face.init_face_verification(VERIFICATION_API_KEY)

image_path: str = 'examples/common/jonathan-petit-unsplash.jpg'

verify.verify(source_image_path=image_path, target_image_path=image_path)
```

## Reference

### CompreFace Global Object

Global CompreFace Object is used for initializing connection to CompreFace and setting default values for options.
Default values will be used in every service method if applicable.
If the option’s value is set in the global object and passed as a function argument then the function argument value will be used.

**Constructor:**

```CompreFace(domain, port, options)```

| Argument | Type   | Required | Notes                                     | 
| ---------| ------ | -------- | ----------------------------------------- | 
| url      | string | required | URL with protocol where CompreFace is located. E.g. `http://localhost` |
| port     | string | required | CompreFace port. E.g. `8000` |
| options  | object | optional | Default values for face recognition services. See more [here](#options-structure). `AllOptionsDict` object can be used in this method   |

Possible options:

| Option              | Type    | Notes                                     |
| --------------------| ------  | ----------------------------------------- |
| det_prob_threshold  | string  | minimum required confidence that a recognized face is actually a face. Value is between 0.0 and 1.0 |
| limit               | integer | maximum number of faces on the image to be recognized. It recognizes the biggest faces first. Value of 0 represents no limit. Default value: 0       |
| prediction_count    | integer | maximum number of subject predictions per face. It returns the most similar subjects. Default value: 1    |
| face_plugins        | string  | comma-separated slugs of face plugins. If empty, no additional information is returned. [Learn more](https://github.com/exadel-inc/CompreFace/tree/master/docs/Face-services-and-plugins.md)    |
| status              | boolean | if true includes system information like execution_time and plugin_version fields. Default value is false    |

Example:

```python
from compreface import CompreFace

DOMAIN: str = 'http://localhost'
PORT: str = '8000'

compre_face: CompreFace = CompreFace(domain=DOMAIN, port=PORT, options={
    "limit": 0,
    "det_prob_threshold": 0.8,
    "prediction_count": 1,
    "face_plugins": "calculator,age,gender,landmarks",
    "status": "true"
})
```

**Methods:**

1. ```CompreFace.init_face_recognition(api_key)```

Inits face recognition service object.

| Argument | Type   | Required | Notes                                     |
| ---------| ------ | -------- | ----------------------------------------- |
| api_key  | string | required | Face Recognition Api Key in UUID format    |

Example:

```python
from compreface.service import RecognitionService

API_KEY: str = 'your_face_recognition_key'

recognition: RecognitionService = compre_face.init_face_recognition(API_KEY)
```

2. ```CompreFace.init_face_detection(api_key)```

Inits face detection service object.

| Argument | Type   | Required | Notes                                     |
| ---------| ------ | -------- | ----------------------------------------- |
| api_key  | string | required | Face Detection Api Key in UUID format    |

Example:

```python
from compreface.service import DetectionService

DETECTION_API_KEY: str = 'your_face_detection_key'

detection: DetectionService = compre_face.init_face_detection(DETECTION_API_KEY)
```

3. ```CompreFace.init_face_verification(api_key)```

Inits face verification service object.

| Argument | Type   | Required | Notes                                     |
| ---------| ------ | -------- | ----------------------------------------- |
| api_key  | string | required | Face Verification Api Key in UUID format    |

Example:

```python
from compreface.service import VerificationService

VERIFICATION_API_KEY: str = 'your_face_verification_key'

verify: VerificationService = compre_face.init_face_verification(VERIFICATION_API_KEY)
```

### Options structure

Options is optional field in every request that contains an image.
If the option’s value is set in the global object and passed as a function argument then the function argument value will be used.

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

Example of face recognition with object:

```python
recognition.recognize(image_path=image_path, options={
    "limit": 0,
    "det_prob_threshold": 0.8,
    "prediction_count": 1,
    "face_plugins": "calculator,age,gender,landmarks",
    "status": "true"
})
```

### Face Recognition Service

Face recognition service is used for face identification.
This means that you first need to upload known faces to face collection and then recognize unknown faces among them.
When you upload an unknown face, the service returns the most similar faces to it.
Also, face recognition service supports verify endpoint to check if this person from face collection is the correct one.
For more information, see [CompreFace page](https://github.com/exadel-inc/CompreFace).

#### Add an Example of a Subject

This creates an example of the subject by saving images. You can add as many images as you want to train the system.

```python
FaceCollection.add(image_path, subject, options)
```

| Argument           | Type   | Required | Notes                                                                                                |
| ------------------ | ------ | -------- | ---------------------------------------------------------------------------------------------------- |
| image_path         | image  | required | Image can pass from url, local path or bytes. Max size is 5Mb               |
| subject            | string | required | is the name you assign to the image you save                                                         |
| options            | object | optional | `DetProbOptionsDict` object can be used in this method. See more [here](#options-structure).  |

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
RecognitionService.recognize(image_path, options)
```

| Argument           | Type    | Required | Notes                                                                                                                                          |
| ------------------ | ------- | -------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| image_path         | image   | required | Image can pass from url, local path or bytes. Max size is 5Mb                                                         |
| options            | object  | optional | `AllOptionsDict` object can be used in this method. See more [here](#options-structure).  |

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

| Argument  | Type   | Required | Notes                                                                                                                                |
| --------- | ------ | -------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| subject   | string | optional | is the name you assign to the image you save. If this parameter is absent, all faces in Face Collection will be removed |

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
| Argument  | Type   | Required | Notes                                                        |
| --------- | ------ | -------- | ------------------------------------------------------------ 
| image_id  | UUID   | required | UUID of the removing face                                    |

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

```python
FaceCollection.verify(image_path, image_id, options)
```

Compares similarities of given image with image from your face collection.


| Argument           | Type    | Required | Notes                                                                                                                                                 |
| ------------------ | ------- | -------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| image_path         | image   | required | Image can pass from url, local path or bytes. Max size is 5Mb                                                                |
| image_id           | UUID    | required | UUID of the verifying face                                                                                                                            |
| options            | string  | Object   | `ExpandedOptionsDict` object can be used in this method. See more [here](#options-structure).  |

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

### Face Detection Service

Face detection service is used for detecting faces in the image.

**Methods:**

#### Detect

```python
DetectionService.detect(image_path, options)
```

Finds all faces on the image.

| Argument          | Type    | Required | Notes                                                                                                                                          |
| ----------------- | ------- | -------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| image_path        | image   | required | image where to detect faces. Image can pass from url, local path or bytes. Max size is 5Mb                            |
| options           | string  | Object   | `ExpandedOptionsDict` object can be used in this method. See more [here](#options-structure).  |

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

Face verification service is used for comparing two images.
A source image should contain only one face which will be compared to all faces on the target image.

**Methods:**

```python
VerificationService.verify(source_image_path, target_image_path, options)
```

Compares two images provided in arguments. Source image should contain only one face, it will be compared to all faces in the target image.

| Argument            | Type    | Required | Notes                                                                                                                                                 |
| ------------------  | ------- | -------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| image_id            | UUID    | required | UUID of the verifying face                                                                                                                            |
| source_image_path   | image   | required | file to be verified. Image can pass from url, local path or bytes. Max size is 5Mb                                           |
| target_image_path   | image   | required | reference file to check the source file. Image can pass from url, local path or bytes. Max size is 5Mb                       |
| options             | string  | Object   | `ExpandedOptionsDict` object can be used in this method. See more [here](#options-structure).  |

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

# Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are greatly appreciated.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

After creating your first contributing pull request, you will receive a request to sign our Contributor License Agreement by commenting your pull request with a special message.

### Report Bugs

Please report any bugs [here](https://github.com/exadel-inc/compreface-python-sdk/issues).

If you are reporting a bug, please specify:

- Your operating system name and version
- Any details about your local setup that might be helpful in troubleshooting
- Detailed steps to reproduce the bug

### Submit Feedback

The best way to send us feedback is to file an issue at https://github.com/exadel-inc/compreface-python-sdk/issues.

If you are proposing a feature, please:

- Explain in detail how it should work.
- Keep the scope as narrow as possible to make it easier to implement.

# License info

CompreFace Python SDK is open-source facial recognition SDK released under the [Apache 2.0 license](https://www.apache.org/licenses/LICENSE-2.0.html).
