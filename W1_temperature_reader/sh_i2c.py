#!/usr/bin/env python3

import subprocess

class I2C_client:
    """ Reading and writing to i2c wrapper """
    def __init__(self, bus, address):
        self.address = address
        self.bus = bus

    def readByte(self, register = 0xff):
        command = ['i2cget', '-y', hex(self.bus), hex(self.address)]
        if register != 0xff:
            command.append(hex(register))
            result = subprocess.run(command, capture_output=True, text=True)
        else:
            result = subprocess.run(command, capture_output=True, text=True)
           
        return int(result.stdout, base=16)

    def WriteByte(self, address, data=None):
        if data:
            command = ['i2cset', '-y', '-f', str(self.bus), hex(self.address), hex(address), hex(data)]
        else:
            command = ['i2cset', '-y', '-f', str(self.bus), hex(self.address), hex(address)]

        result = subprocess.run(command, capture_output=True, text=True)

        if 'Error' in result.stdout or 'Error' in result.stderr:
            return False
        else:
            return True
        



    

    
        


