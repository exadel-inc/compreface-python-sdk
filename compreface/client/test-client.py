import requests
import os
from requests_toolbelt.multipart.encoder import MultipartEncoder

url_view = "http://localhost:8000/api/v1/faces"
api_key = "7dacfc8e-1bb1-4fcf-a9b1-76e4d9d89855"
headers = {"Content-Type": "application/x-www-form-urlencoded", "x-api-key": api_key}
headers_api_key = {"x-api-key": api_key}
path = 'image_path'


def add(path_img, subject):
    url = 'http://localhost:8000/api/v1/faces?subject=' + subject
    name_img = os.path.basename(path_img)
    m = MultipartEncoder(
        fields={'file': (name_img, open(path_img, 'rb'))}
    )

    r = requests.post(url, data=m, headers={'Content-Type': m.content_type,
                                            'x-api-key': api_key})

    print(r.status_code)
    print(r.text)
    print(r.json())