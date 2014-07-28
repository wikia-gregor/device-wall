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

        if self.factory.avaiable_devices is None:
            self.updateDevicesList()

    def connectionMade(self):
        self.transport.write('Welcome to Devices Manager!\nTry `help` if you don\'t know what to do ;-)\n')

    def lineReceived(self, line):
        """Received line from client - parse it and do something with it"""
        command_regex = '^(?P<command>list|lock|unlock|help)(\s(?P<param>.*))?'
        regex = re.compile(command_regex)
        matches = regex.match(line)

        if matches is None:
            print('Unknown command: "' + line + '"')
            self.sendLine('Sorry dude, but I don\'t understand this command.')
            return

        command = matches.group('command')

        if command is not None:
            if command == 'list':
                self.listDevices()

            if command == 'lock':
                device_id = matches.group('param')
                if device_id is not None:
                    print('locking param: ' + device_id)
                    self.lockDevice(device_id)
                else:
                    self.sendLine('Device id is required.')

            if command == 'unlock':
                device_id = matches.group('param')
                if device_id is not None:
                    self.unlockDevice(matches.group('param'))
                else:
                    self.sendLine('Device id is required.')

            if command == 'help':
                self.sendHelp()

    def updateDevicesList(self):
        """Load devices list via instruments"""
        print('update devices list')

    def listDevices(self):
        """Return list of all devices"""
        print('list devices')

    def lockDevice(self, device_id):
        """Lock device (eg. run tests on device)"""
        print('lock device with id: ' + device_id)

    def unlockDevice(self, device_id):
        """Unlock device (eg. tests on device finished"""
        print('unlock device with id: ' + device_id)

    def sendHelp(self):
        """Return list of available commands"""
        print('send help message')


class ServiceFactory(Factory):
    """Devices Manager Service Factory"""
    def __init__(self):
        self.available_devices = []

    def buildProtocol(self, addr):
        return Service(self)


def run_service():
    """Running devices manager service"""
    print('Devices Manager Service starting...')
    reactor.listenTCP(8012, ServiceFactory())
    print(' Done! (listening on port 8012)')
    reactor.run()

