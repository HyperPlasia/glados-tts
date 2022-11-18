import os

import pkg_resources
from setuptools import setup, find_packages

setup(
    name="glados-tts",
    version="1.0.1",
    license="MIT",
    url='https://github.com/R2D2FISH/glados-tts',
    description="frok of https://github.com/R2D2FISH/glados-tts",
    author="https://github.com/R2D2FISH/glados-tts/graphs/contributors",
    py_modules=["."],
    packages=["."],
    requires=[
        str(r)
        for r in pkg_resources.parse_requirements(
            open(os.path.join(os.path.dirname(__file__), "requirements.txt"))
        )
    ]
)
