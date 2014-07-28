__author__ = 'wikia-gregor'

from subprocess import check_output
import re


class Instruments():

    def __init__(self):
        pass

    def is_simulator(self, description_string):
        pass

    def is_device(self, description_string):
        pass


def testing_regex():
    dev_string = [
        'iPhone 5 Mr G. (v7.1.2) (abcdefghijklmnopqrstuvwxyz1234567890123x)',
        'iPad (wikia-gregor) (v8.0) (abcdefghijklmnopqrstuvwxyz1234567890123x)',
        'Alistra\'s Apple 5S (v8.0) (abcdefghijklmnopqrstuvwxyz1234567890123x)',
    ]

    sim_strings = [
        'iPhone Retina (4-inch 64-bit) - Simulator - iOS 6.1',
        'iPhone Retina (3.5-inch) - Simulator - iOS 6.1',
        'iPad Retina (64-bit) - Simulator - iOS 7.1',
        'iPad Retina - Simulator - iOS 7.1',
    ]

    regex_string = _device_regexp()
    # regex_string = _simulator_regexp()
    regex = re.compile(regex_string)
    print('regex: ' + regex_string)

    # for string in sim_strings:
    for string in dev_string:
        print('String to test: ' + string)
        matches = regex.match(string)

        if matches is None:
            print(' Regex ERROR!')

        else:
            print(' String parts:')
            x = 1
            for group in matches.groups():
                if group is not None:
                    print('  ' + x.__str__() + ': ' + group.__str__())
                x += 1
        print(' ')


def _simulator_regexp():
    r_name = '^(?P<name>.*?)'
    r_type = '(?:\s\\((?:(?P<size>.*inch))?\s?(?:(?P<arch>.*bit))?\\))?'
    r_sim = '\s\\-\sSimulator\s\\-\s'
    r_version = 'iOS\s(?P<version>.*)$'
    return r_name + r_type + r_sim + r_version


def _device_regexp():
    r_name = '^(?P<name>.*?)'
    r_version = '\\(v(?P<version>.*)\\)'
    r_uuid = '\\((?P<uuid>[a-z0-9]{40})\\)$'
    return r_name + '\s' + r_version + '\s' + r_uuid


def instruments_read_devices():
    list_of_devices = check_output(['instruments', '-s', 'devices'])
    lines = list_of_devices.splitlines()
    simulator_regex = re.compile(_simulator_regexp())
    device_regex = re.compile(_device_regexp())

    for line in lines:
        print('checking line: ' + line)
        dev_match = device_regex.match(line)

        if dev_match is not None:
            device_from_match(dev_match)
            continue

        sim_match = simulator_regex.match(line)

        if sim_match is not None:
            # simulator_device_from_match(sim_match)
            continue


def device_from_match(match):
    print('This is Device!')


def simulator_device_from_match(match):
    print('This is Simulator!')