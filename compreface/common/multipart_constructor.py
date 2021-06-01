import os
import requests

from requests_toolbelt.multipart.encoder import MultipartEncoder


def get_file(image: str = '' or bytes):
    if not os.path.isfile(image):
        if type(image) != bytes:
            response = requests.get(image)
            file = response.content
        else:
            file = image
        file = ('image.jpg', file)
    else:
        name_img: str = os.path.basename(image)
        file = (name_img, open(image, 'rb'))
    return file


def multipart_constructor(image: str = '' or bytes):

    # Encoding image from path and encode in multipart for sending to the server.
    return MultipartEncoder(
        fields={'file': get_file(image)}
    )


def multipart_constructor_with_two_images(source_image: str = '' or bytes, target_image: str = '' or bytes):
    return MultipartEncoder(
        fields={'source_image': get_file(
            source_image), 'target_image': get_file(target_image)}
    )
