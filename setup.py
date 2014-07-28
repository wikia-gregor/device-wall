from setuptools import setup, find_packages
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
    packages=find_packages(),
    install_requires=[
        'Flask==0.10.1',
        'enum34==1.0',
        'Twisted==14.0.0'
    ],
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'list_devices=dw.devices_manager.service:list_devices',
            'devices_manager=dw.devices_manager.service:run_service',
            'run_panel=dw.web_panel.app:run_panel'
        ],
    }
)
