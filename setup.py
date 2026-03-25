from setuptools import setup, find_packages
from typing import List 

import os
from typing import List

def get_requirements(file_path: str) -> List[str]:
    requirements = []

    base_path = os.path.dirname(__file__)
    full_path = os.path.join(base_path, file_path)

    with open(full_path) as file:
        requirements = file.readlines()
        requirements = [req.strip() for req in requirements]

    # remove '-e .'
    requirements = [req for req in requirements if req != "-e ."]

    return requirements


setup(
    name="ML-Project",
    version="0.0.1",
    author="Umesh",
    author_email="umeshyadavtds@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")
)