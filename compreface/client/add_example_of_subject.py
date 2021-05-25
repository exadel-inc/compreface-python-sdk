# -*- coding: utf-8 -*-

from compreface.common.typed_dict import DetProbOptionsDict, check_fields_by_name
from compreface.config.api_list import RECOGNIZE_CRUD_API
import os
import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder

from ..common import ClientRequest


class AddExampleOfSubjectClient(ClientRequest):

    def __init__(self, api_key: str, domain: str, port: str):
        super().__init__()
        self.client_url: str = RECOGNIZE_CRUD_API
        self.api_key: str = api_key
        self.url: str = domain + ':' + port + self.client_url

    """
        GET request for get all subjects. 
        
        :return: json with subjects from server.
    """

    def get(self) -> dict:
        url: str = self.url
        result = requests.get(url, headers={'x-api-key': self.api_key})
        return result.json()

    """
        POST request for add subject from his face in image. 
        
        :param image_path: path to image in file system.
        :param subject: fullname
        :param options: dictionary with options for server.
        
        :return: json with this subject from server.
    """

    def post(self, image_path: str = '', subject: str = '', options: DetProbOptionsDict = {}) -> dict:
        url: str = self.url + '?subject=' + subject
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

        # Sending encode image for add subject.
        result = requests.post(url, data=m, headers={'Content-Type': m.content_type,
                                                     'x-api-key': self.api_key})
        return result.json()

    def put(self):
        pass

    """ 
        Delete request to CompreFace server. 
        
        :param subject: fullname
        
        :return: json from server.
    """

    def delete(self, subject: str = ''):
        url: str = self.url + '?subject=' + subject
        result = requests.delete(url, headers={'x-api-key': self.api_key})
        return result.json()
