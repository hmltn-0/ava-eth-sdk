# setup.py

from setuptools import setup, find_packages

setup(
    name='ava-eth-sdk',
    version='0.1.0',
    author='Julius Hamilton',
    author_email='juliushamilton100@gmail.com',
    description='A Python SDK for interacting with Ava Protocol and Ethereum networks',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/hmltn-0/ava-eth-sdk',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'grpcio',
        'web3',
        'eth-account',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',  # Update if using a different license
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)

