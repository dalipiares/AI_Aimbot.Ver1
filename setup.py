from setuptools import setup, find_packages
import os

def parse_requirements(filename):
    with open(filename, 'r') as file:
        return file.read().splitlines()

setup(
    name='ScreenObjectDetection',
    version='1.0.0',
    packages=find_packages(),
    install_requires=parse_requirements(os.path.join(os.path.dirname(__file__), 'requirements.txt')),
    dependency_links=[
        'git+https://github.com/ultralytics/yolov5.git#egg=yolov5',
        'https://download.pytorch.org/whl/cu118/torch_stable.html',
    ],
    description='Real-time screen object detection using YOLOv5 and CUDA',
    author='dalipiares',
    author_email='ares.dalipi@stud.edubs.ch',
    url='https://github.com/dalipiares/Roblox_1',
)