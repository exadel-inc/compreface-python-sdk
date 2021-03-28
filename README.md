# CompreFace Python-SDK

CompreFace is free and open-source face recognition system from Exadel and this Python SDK helps you to use all functionalities of the system in your application without prior skills.

## Content
- [Installation](#installation)
- [Recognition Service](#recognition)
- [Usage](#usage)


## Rest API description

By using the created API key, the user can add an image as an example of a particular face, retrieve a list of saved images, recognize a face from the image uploaded to the Face Collection, and delete all examples of the face by the name.

## Installation

Run below command to install SDK in your environment.
```python
 pip install compreface
```

## Recognition Service

### Add an Example of a Subject

This creates an example of the subject by saving images. You can add as many images as you want to train the system.

```python 
FaceCollection.add(file, subject)
```
| Element             | Description | Type   | Required | Notes                                                        |
| ------------------- | ----------- | ------ | -------- | ------------------------------------------------------------ |
| subject             | param       | string | required | is the name you assign to the image you save                 |
| file                | body        | image  | required | allowed image formats: jpeg, jpg, ico, png, bmp, gif, tif, tiff, webp. Max size is 5Mb |

Response body on success:
```
{
  "image_id": "<UUID>",
  "subject": "<subject>"
}
```

| Element  | Type   | Description                |
| -------- | ------ | -------------------------- |
| image_id | UUID   | UUID of uploaded image     |
| subject  | string | <subject> of saved image |



### Recognize Faces from a Given Image

Recognizes faces from the uploaded image.
```python
RecognitionService.recognize(file, limit, det_prob_threshold, prediction_count)
```


| Element          | Description | Type    | Required | Notes                                                        |
| ---------------- | ----------- | ------- | -------- | ------------------------------------------------------------ |
| file             | body        | image   | required | allowed image formats: jpeg, jpg, ico, png, bmp, gif, tif, tiff, webp. Max size is 5Mb |
| limit            | param       | integer | optional | maximum number of faces with best similarity in result. Value of 0 represents no limit. Default value: 0 |
| det_prob_ threshold | param       | string | optional | minimum required confidence that a recognized face is actually a face. Value is between 0.0 and 1.0. |
| prediction_count | param       | integer | optional | maximum number of predictions per faces. Default value: 1    |

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
      "faces": [
        {
          "similarity": <similarity1>,
          "subject": <subject1>	
        },
        ...
      ]
    }
  ]
}
```

| Element                        | Type    | Description                                                  |
| ------------------------------ | ------- | ------------------------------------------------------------ |
| box                            | object  | list of parameters of the bounding box for this face         |
| probability                    | float   | probability that a found face is actually a face             |
| x_max, y_max, x_min, y_min | integer | coordinates of the frame containing the face                 |
| faces                          | list    | list of similar faces with size of <prediction_count> order by similarity |
| similarity                     | float   | similarity that on that image predicted person              |
| subject                        | string  | name of the subject in Face Collection                                 |



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

| Element  | Type   | Description                                                  |
| -------- | ------ | ------------------------------------------------------------ |
| image_id | UUID   | UUID of the face                                             |
| subject  | string | <subject> of the person, whose picture was saved for this api key |


### Delete All Examples of the Subject by Name

To delete all image examples of the <subject>:

```python 
FaceCollection.delete_all(subject)
```

| Element   | Description | Type   | Required | Notes                                                        |
| --------- | ----------- | ------ | -------- | ------------------------------------------------------------ |
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

| Element  | Type   | Description                                                  |
| -------- | ------ | ------------------------------------------------------------ |
| image_id | UUID   | UUID of the removed face                                     |
| subject  | string | <subject> of the person, whose picture was saved for this api key |



### Delete an Example of the Subject by ID

To delete an image by ID:

```python 
FaceCollection.delete(image_id)
```

| Element   | Description | Type   | Required | Notes                                     |
| --------- | ----------- | ------ | -------- | ----------------------------------------- |
| image_id  | variable    | UUID   | required | UUID of the removing face                 |

Response body on success:
```
{
  "image_id": <image_id>,
  "subject": <subject>
}
```

| Element  | Type   | Description                                                  |
| -------- | ------ | ------------------------------------------------------------ |
| image_id | UUID   | UUID of the removed face                                     |
| subject  | string | <subject> of the person, whose picture was saved for this api key |



### Verify Faces from a Given Image

To compare faces from the uploaded images with the face in saved image ID:
```python 
RecognitionService.verify(image_id, file, limit, det_prob_threshold)
```


| Element          | Description | Type    | Required | Notes                                                        |
| ---------------- | ----------- | ------- | -------- | ------------------------------------------------------------ |
| image_id         | variable    | UUID    | required | UUID of the verifying face                                   |
| file             | body        | image   | required | allowed image formats: jpeg, jpg, ico, png, bmp, gif, tif, tiff, webp. Max size is 5Mb |
| limit            | param       | integer | optional | maximum number of faces with best similarity in result. Value of 0 represents no limit. Default value: 0 |
| det_prob_threshold | param       | string | optional | minimum required confidence that a recognized face is actually a face. Value is between 0.0 and 1.0. |

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

| Element                        | Type    | Description                                                  |
| ------------------------------ | ------- | ------------------------------------------------------------ |
| box                            | object  | list of parameters of the bounding box for this face         |
| probability                    | float   | probability that a found face is actually a face             |
| x_max, y_max, x_min, y_min     | integer | coordinates of the frame containing the face                 |
| similarity                     | float   | similarity that on that image predicted person               |
| subject                        | string  | name of the subject in Face Collection                       |

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
```

### Example Add an Example of a Subject

This creates an example of the subject by saving images. You can add as many images as you want to train the system.

```python 
from compreface import CompreFace
from compreface.service import RecognitionService
from compreface.collections import FaceColliction


DOMAIN: str = 'http://localhost'
PORT: str = '8000'
API_KEY: str = '7dacfc8e-1bb1-4fcf-a9b1-76e4d9d89855'


compre_face: CompreFace = CompreFace(DOMAIN, PORT)

recognition: RecognitionService = compre_face.init_face_recognition(API_KEY)

face_collection: FaceColliction = recognition.get_face_collection()

image_path: str = '/some/path/some_image.jpg'
subject: str = 'test'
result = face_collection.add(image_path, subject)
```


### Example Recognize Faces from a Given Image 

Recognizes faces from the uploaded image.
```python
from compreface import CompreFace
from compreface.service import RecognitionService


DOMAIN: str = 'http://localhost'
PORT: str = '8000'
API_KEY: str = '7dacfc8e-1bb1-4fcf-a9b1-76e4d9d89855'


compre_face: CompreFace = CompreFace(DOMAIN, PORT)

recognition: RecognitionService = compre_face.init_face_recognition(API_KEY)

image_path: str = '/some/path/some_iamge.jpg'

result = recognition.recognize(image_path)

```

### Example List of All Saved Subjects 

To retrieve a list of subjects saved in a Face Collection:

```python
from compreface import CompreFace
from compreface.service import RecognitionService
from compreface.collections import FaceColliction


DOMAIN: str = 'http://localhost'
PORT: str = '8000'
API_KEY: str = '7dacfc8e-1bb1-4fcf-a9b1-76e4d9d89855'


compre_face: CompreFace = CompreFace(DOMAIN, PORT)

recognition: RecognitionService = compre_face.init_face_recognition(API_KEY)

face_collection: FaceColliction = recognition.get_face_collection()

result = face_collection.list()
```

### Example Delete All Examples of the Subject by Name 

To delete all image examples of the <subject>:

```python 
from compreface import CompreFace
from compreface.service import RecognitionService
from compreface.collections import FaceColliction


DOMAIN: str = 'http://localhost'
PORT: str = '8000'
API_KEY: str = '7dacfc8e-1bb1-4fcf-a9b1-76e4d9d89855'


compre_face: CompreFace = CompreFace(DOMAIN, PORT)

recognition: RecognitionService = compre_face.init_face_recognition(API_KEY)
subject: str = 'test'

face_collection: FaceColliction = recognition.get_face_collection()

result = recognition.delete_all(subject)
```


### Example Delete an Example of the Subject by ID 

To delete an image by ID:

```python 
from compreface import CompreFace
from compreface.service import RecognitionService
from compreface.collections import FaceColliction


DOMAIN: str = 'http://localhost'
PORT: str = '8000'
API_KEY: str = '7dacfc8e-1bb1-4fcf-a9b1-76e4d9d89855'


compre_face: CompreFace = CompreFace(DOMAIN, PORT)

recognition: RecognitionService = compre_face.init_face_recognition(API_KEY)
image_id: str = '3aff54a4-862b-48e5-a5e1-10056cc893da'

face_collection: FaceColliction = recognition.get_face_collection()

result = face_collection.delete(image_id)

```

### Example Verify Faces from a Given Image 

To compare faces from the uploaded images with the face in saved image ID:
```python 
from compreface import CompreFace
from compreface.service import RecognitionService


DOMAIN: str = 'http://localhost'
PORT: str = '8000'
API_KEY: str = '7dacfc8e-1bb1-4fcf-a9b1-76e4d9d89855'


compre_face: CompreFace = CompreFace(DOMAIN, PORT)

verification: RecognitionService = compre_face.init_face_recognition(API_KEY)

image_path: str = '/some/path/some_image.jpg'
image_id: str = '3aff54a4-862b-48e5-a5e1-10056cc893da'

result = verification.verify(image_path, image_id)
```

All this examples you can find in repozitory inside "examples" folder.