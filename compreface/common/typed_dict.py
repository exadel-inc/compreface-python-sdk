from compreface.exceptions import IncorrectFieldException
from typing import Any, TypedDict


class DetProbOptionsDict(TypedDict):
    det_prob_threshold: float


class ExpandedOptionsDict(DetProbOptionsDict):
    limit: int
    prediction_count: int
    status: bool


class AllOptionsDict(ExpandedOptionsDict):
    face_plugins: str


""" 
    Checks fields with necessary rules.
    :param name: key from dictionary.
    :param value: value from dictionary.
    
    raise exception when value break necessary rules.
"""


def check_fields_by_name(name: str, value: Any):
    if name == 'limit' or name == "prediction_count":
        if value < 0:
            raise IncorrectFieldException(
                '{} must be greater or equal zero.'.format(name))
    if name == 'det_prob_threshold':
        if value < 0.0 or value > 1.0:
            raise IncorrectFieldException(
                'det_prob_threshold must be between 0.0 and 1.0. Received value {}'.format(value))
    if name == "face_plugins":
        values = value.strip()
        for row in values.split(','):
            if row == ',':
                pass
            if row.find('age') == -1 and row.find('calculator') == -1 and row.find('gender') == -1 and row.find('landmarks') == -1:
                raise IncorrectFieldException(
                    "face_plugins must be only contains calculator,age,gender,landmarks. Incorrect value {}".format(row))
