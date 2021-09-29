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


from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='compreface-sdk',
    packages=find_packages(exclude=("tests",)),
    version='0.6.0',
    license='Apache License 2.0',
    description='CompreFace Python SDK makes face recognition into your application even easier.',
	long_description=long_description,
	long_description_content_type="text/markdown",
    author='Artsiom Liubymov aliubymov@exadel.com, Artsiom Khadzkou akhadzkou@exadel.com, Aliaksei Tauhen atauhen@exadel.com',
    author_email='aliubymov@exadel.com, akhadzkou@exadel.com, atauhen@exadel.com',
    url='https://exadel.com/solutions/compreface/',
    download_url='https://github.com/exadel-inc/compreface-python-sdk/archive/refs/tags/0.6.0.tar.gz',
    keywords=[
        "CompreFace",
        "Face Recognition",
        "Face Detection",
        "Face Verification",
        "Face Identification",
        "Computer Vision",
        "SDK"
    ],
    install_requires=[
        'requests-toolbelt==0.9.1'
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Intended Audience :: Information Technology',
        'Topic :: Software Development',
        'Topic :: Software Development :: Build Tools',
        'Topic :: Software Development :: Libraries',
        'Topic :: Scientific/Engineering :: Image Recognition',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7'
    ],
)
