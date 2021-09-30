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


RECOGNITION_ROOT_API: str = '/api/v1/recognition'

RECOGNIZE_API: str = RECOGNITION_ROOT_API + '/recognize'
RECOGNIZE_CRUD_API: str = RECOGNITION_ROOT_API + '/faces'
SUBJECTS_CRUD_API: str = RECOGNITION_ROOT_API + '/subjects'

DETECTION_API: str = '/api/v1/detection/detect'

VERIFICATION_API: str = '/api/v1/verification'
