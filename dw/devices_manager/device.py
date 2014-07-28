__author__ = 'wikia-gregor'

from enum import Enum


class Type(Enum):
    """Device type"""
    simulator = 1
    phone = 2
    tablet = 3


class OsType(Enum):
    """Device OS type"""
    ios = 1
    android = 2


class Device():
    """Device model"""

    def __init__(self, name, device_type, os_type, os_version, arch):
        self.name = name
        self.device_type = device_type  # simulator, phone, tablet
        self.os_type = os_type  # ios, android
        self.os_version = os_version
        self.serial_number = ''
        self.arch = arch
        self.additional_info = {}


def device_from_match():
    pass

