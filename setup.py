import os

import pkg_resources
from setuptools import setup

setup(
    name="glados-tts",
    version="1.0.2",
    license="MIT",
    url='https://github.com/R2D2FISH/glados-tts',
    description="fork of https://github.com/R2D2FISH/glados-tts",
    author="https://github.com/R2D2FISH/glados-tts/graphs/contributors",
    py_modules=["glados"],
    packages=["glados"],
    requires=[
        str(r)
        for r in pkg_resources.parse_requirements(
            open(os.path.join(os.path.dirname(__file__), "requirements.txt"))
        )
    ]
)
