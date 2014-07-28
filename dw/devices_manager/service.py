__author__ = 'wikia-gregor'
from twisted.protocols.basic import LineReceiver
from twisted.internet.protocol import Factory
from twisted.internet import reactor
import re
import instruments


class Service(LineReceiver):
    """Devices Manager Service"""

    def __init__(self, factory):
        self.factory = factory

        if self.factory.available_devices is None:
            self.updateDevicesList()

    def connectionMade(self):
        self.transport.write('Welcome to Devices Manager!\nTry `help` if you don\'t know what to do ;-)\n')

    def lineReceived(self, line):
        """Received line from client - parse it and do something with it"""
        command_regex = '^(?P<command>list|status|lock|unlock|help)(\s(?P<param>.*))?'
        regex = re.compile(command_regex)
        matches = regex.match(line)

        if matches is None:
            print('Unknown command: "' + line + '"')
            self.sendLine('Sorry dude, but I don\'t understand this command.')
            return

        command = matches.group('command')
        device_id = matches.group('param')

        if command is not None:
            if command == 'list':
                self.listDevices()

            if command == 'status':
                self.status()

            if command == 'lock':
                if device_id is not None:
                    self.lockDevice(device_id)
                else:
                    self.sendLine('Device ID is required.')

            if command == 'unlock':
                if device_id is not None:
                    self.unlockDevice(matches.group('param'))
                else:
                    self.sendLine('Device ID is required.')

            if command == 'help':
                self.sendHelp()

    def updateDevicesList(self):
        """Load devices list via instruments"""
        self.factory.available_devices = instruments.instruments_read_devices()

    def listDevices(self):
        """Return list of all devices"""
        print('list devices')
        self.sendLine(self.factory.available_devices.__str__())

    def status(self):
        """Return status of all devices"""
        print('status')
        self.sendLine('status!')

    def lockDevice(self, device_id):
        """Lock device (eg. run tests on device)"""
        print('lock device with id: ' + device_id)

    def unlockDevice(self, device_id):
        """Unlock device (eg. tests on device finished"""
        print('unlock device with id: ' + device_id)

    def sendHelp(self):
        """Return list of available commands"""
        print('send help message')
        self.sendLine('\nDevices Manager\n'
                      '  Available commands:\n'
                      '  help               - display this awesome help message\n'
                      '  list               - list all connected devices\n'
                      '  lock <device_id>   - lock device with given id\n'
                      '  unlock <device_id> - unlock device with given id\n')


class ServiceFactory(Factory):
    """Devices Manager Service Factory"""
    def __init__(self):
        self.available_devices = instruments.instruments_read_devices()

    def buildProtocol(self, addr):
        return Service(self)


def run_service():
    """Running devices manager service"""
    print('Devices Manager Service starting...')
    reactor.listenTCP(8012, ServiceFactory())
    print(' Done! (listening on port 8012)')
    reactor.run()

