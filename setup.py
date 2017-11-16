from setuptools import setup

setup(
    name='mergeimages',
    author='ognjetina',
    author_email='laogdo@gmail.com',
    version='0.1',
    scripts=['mergeimages'],
    install_requires=['image', 'olefile', 'Pillow', 'pytz'],
    classifiers=['Programming Language:: Python:: 3.6']
)
