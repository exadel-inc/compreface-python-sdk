import pytest
import httpretty
import requests
from compreface.client.delete_example_by_id import DeleteExampleByIdClient
from compreface.config.api_list import RECOGNIZE_CRUD_API
from tests.client.const_config import DOMAIN, PORT, RECOGNIZE_API_KEY, IMAGE_ID

"""
    Server configuration.
    url: string = DOMAIN:PORT/API/IMAGE_ID
"""
url: str = DOMAIN + ":" + PORT + RECOGNIZE_CRUD_API + '/' + IMAGE_ID


@httpretty.activate(verbose=True, allow_net_connect=False)
def test_delete():
    httpretty.register_uri(
        httpretty.DELETE,
        url,
        headers={'x-api-key': RECOGNIZE_API_KEY},
        body='{"image_id": "image_id", "subject": "Donatello"}'
    )
    response: dict = requests.delete(
        url=url, headers={'x-api-key': RECOGNIZE_API_KEY}).json()

    test_subject: DeleteExampleByIdClient = DeleteExampleByIdClient(
        RECOGNIZE_API_KEY, DOMAIN, PORT)
    test_response: dict = test_subject.delete(IMAGE_ID)
    assert response, test_response
