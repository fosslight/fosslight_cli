# setup.py
from setuptools import setup, find_packages

with open('requirements.txt', 'r') as f:
    required = f.read().splitlines()


setup(
    name='fosslight_cli',
    version='0.0.1',
    packages=find_packages(),
    install_requires=required,
    python_requires=">=3.8",
    entry_points={
        'console_scripts': [
            "fosslight-cli = src.main:main",
        ]
    }
)
