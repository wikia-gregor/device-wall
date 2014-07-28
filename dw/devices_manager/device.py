__author__ = 'wikia-gregor'

from enum import Enum


class Type(Enum):
    """Device type"""
    simulator = 1
    phone = 2
    tablet = 3

    def __repr__(self):
        if self.value == 1:
            return 'Simulator'
        if self.value == 2:
            return 'Phone'
        if self.value == 3:
            return 'Tablet'


class OsType(Enum):
    """Device OS type"""
    ios = 1
    android = 2

    def __repr__(self):
        if self.value == 1:
            return 'iOS'
        if self.value == 2:
            return 'Android'


class Device():
    """Device model"""

    def __init__(self, name, device_type, os_type, os_version=None, arch=None):
        self.name = name
        self.device_type = device_type  # simulator, phone, tablet
        self.os_type = os_type  # ios, android
        self.os_version = os_version
        self.serial_number = ''
        self.arch = arch
        self.additional_info = {}

    def __repr__(self):
        return self.name + ' (' + self.os_version + ') [' + \
            self.os_type.__repr__() + ', ' + self.device_type.__repr__() + ']'


class Tablet(Device):
    def __init__(self, name, serial_number, os_type, os_version=None, arch=None):
        Device.__init__(self, name, Type.tablet, os_type, os_version, arch)
        self.serial_number = serial_number


class Phone(Device):
    def __init__(self, name, serial_number, os_type, os_version=None, arch=None):
        Device.__init__(self, name, Type.phone, os_type, os_version, arch)
        self.serial_number = serial_number


class Simulator(Device):
    def __init__(self, name, os_type, os_version=None, arch=None):
        Device.__init__(self, name, Type.simulator, os_type, os_version, arch)


class iPhone(Phone):
    def __init__(self, name, serial_number, os_version=None, arch=None):
        Phone.__init__(self, name, serial_number, OsType.ios, os_version, arch)


class iPad(Tablet):
    def __init__(self, name, serial_number, os_version=None, arch=None):
        Tablet.__init__(name, serial_number, OsType.ios, os_version, arch)

