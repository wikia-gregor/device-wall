from setuptools import setup
from dw import __version__, __author__

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='Device Wall',
    version=__version__,
    description='Device Wall - new way of running automation tests',
    long_description=long_description,
    url='https://github.com/wikia-gregor/device-wall',
    author=__author__,
    author_email='grzegorz@wikia-inc.com',
    packages=['dw'],  # can be find_packages()
    install_requires=[
        'Flask==0.10.1',
    ],
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'device-manager=weather.app:run'
        ],
    }
)
