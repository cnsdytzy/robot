import ConfigParser, os
import pygamedisplay

class Configurator:
    def __init__(self, file):
        config = ConfigParser.ConfigParser()

        config.readfp(open(file))

        self.conf = {}

        section = 'network'
        self.conf[section] = { 'address' : config.get(section, 'address'),
                          'port' : int(config.get(section, 'port'))}

        section = 'controls'
        self.conf[section] = { 'stop'   : self._parseControl(config.get(section, 'stop')),
                               'up'     : self._parseControl(config.get(section, 'up')),
                               'down'  : self._parseControl(config.get(section, 'down')),
                               'left'   : self._parseControl(config.get(section, 'left')),
                               'right'  : self._parseControl(config.get(section, 'right')),
                               'rotate_left'  : self._parseControl(config.get(section, 'rotate_left')),
                               'rotate_right' : self._parseControl(config.get(section, 'rotate_right'))}

    def _parseControl(self, controlString):
        if len(controlString) >= 5:
            return self._parseTupleOfInts(controlString)
        elif controlString.find('A') == 0:
            return int(controlString.strip('A'))
        else:
            return int(controlString)


    def _parseTupleOfInts(self, tupleString):
        tupleString = tupleString.strip('(')
        tupleString = tupleString.strip(')')
        tupleList = tupleString.split(',')
        tupleList = [int(item) for item in tupleList]
        return tuple(tupleList)



def main():
    config = Configurator("./controller.cfg")

    network = config.conf['network']
    controls = config.conf['controls']



























if __name__ == '__main__':
    main()