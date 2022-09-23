from setuptools import find_packages, setup

setup(
    name='pylogger',
    packages=find_packages(include=['pylogger']),
    version='0.1.0',
    description='A simple yet powerful library for logging',
    author='Adam',
    license='GNU',
    install_requires=['pytz',''],
)