"""
    Copyright(c) 2021 the original author or authors

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        https: // www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
    or implied. See the License for the specific language governing
    permissions and limitations under the License.
 """

from compreface.exceptions import IncorrectFieldException
from typing import Any, TypedDict


class DetProbOptionsDict(TypedDict):
    det_prob_threshold: float


class ExpandedOptionsDict(DetProbOptionsDict):
    limit: int
    status: bool
    face_plugins: str


class AllOptionsDict(ExpandedOptionsDict):
    prediction_count: int


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
            if row.find('age') == -1 and row.find('calculator') == -1 and row.find('gender') == -1 \
                    and row.find('landmarks') == -1 and row.find('mask') == -1:
                raise IncorrectFieldException(
                    "face_plugins must be only contains calculator,age,gender,landmarks,mask. "
                    "Incorrect value {}".format(row))


def pass_dict(options: AllOptionsDict, type: DetProbOptionsDict or ExpandedOptionsDict):
    converted_options: ExpandedOptionsDict or DetProbOptionsDict = {}
    for key in type.__annotations__.keys():
        value = options.get(key)
        if value != None:
            converted_options[key] = value
    return converted_options
