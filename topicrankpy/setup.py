from setuptools import setup
import os
def readme():
    with open('README.md') as f:
        README = f.read()
    return README


with open('requirements.txt') as f:
    required = f.read().splitlines()


setup(
    name="topicrankpy",
    version="1.0.5",
    description="A Python package to get useful information from documents using TopicRank Algorithm.",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/Aayushpatel007/topic-rank-extract-information",
    author="Aayush Patel",
    author_email="patelaayush678@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["topicrankpy"],
    include_package_data=True,
    install_requires=required
    
)



