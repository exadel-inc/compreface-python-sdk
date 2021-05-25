# -*- coding: utf-8 -*-
import os
import requests
from compreface.common.typed_dict import ExpandedOptionsDict, check_fields_by_name
from compreface.config.api_list import RECOGNIZE_CRUD_API
from requests_toolbelt.multipart.encoder import MultipartEncoder
from ..common import ClientRequest


class CompareFaceFromImageClient(ClientRequest):
    """
        Compare face in image. It uses image path for encode and send to CompreFace 
        server with validation by image id.
    """

    def __init__(self, api_key: str, domain: str, port: str):
        super().__init__()
        self.client_url: str = RECOGNIZE_CRUD_API
        self.api_key: str = api_key
        self.url: str = domain + ':' + port + self.client_url

    def get(self):
        pass

    """
        POST request for compare face in image using image id. 
        
        :param image_path: Path to image in file system.
        :param image_id: subject id from previously added image.
        :param options: dictionary with options for server.
        
        :return: json from server.
    """

    def post(self,
             image_path: str = '',
             image_id: str = '',
             options: ExpandedOptionsDict = {}) -> dict:

        url: str = self.url + '/' + image_id + '/verify?'
        name_img: str = os.path.basename(image_path)
        # Validation loop and adding fields to the url.
        for key in options.keys():
            # Checks fields with necessary rules.
            # key - key field by options.
            check_fields_by_name(key, options[key])
            url += '&' + key + "=" + str(options[key])

        # Encoding image from path and encode in multipart for sending to the server.
        m = MultipartEncoder(
            fields={'file': (name_img, open(image_path, 'rb'))}
        )

        # Sending encode image for verify face.
        result = requests.post(url, data=m, headers={'Content-Type': m.content_type,
                                                     'x-api-key': self.api_key})
        return result.json()

    def put(self):
        pass

    def delete(self):
        pass
