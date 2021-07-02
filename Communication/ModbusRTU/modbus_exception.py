'''
Created on 14.09.2016

@author: Stefan Rossmann
'''


class ModbusException(Exception):
    '''
    classdocs
    '''

    def __init__(self, expression, message):
        """ Exception to be thrown if Modbus Server returns error code "Function Code not executed (0x04)"
        Attributes:
            expression -- input expression in which the error occurred
            message -- explanation of the error
        """
        self.expression = expression
        self.message = message


class SerialPortNotOpenedException(ModbusException):
    '''
    classdocs
    '''

    def __init__(self, expression, message):
        """ Exception to be thrown if serial port is not opened
        Attributes:
            expression -- input expression in which the error occurred
            message -- explanation of the error
        """
        self.expression = expression
        self.message = message


class TimeoutError(Exception):
    def __init__(self, expression, message):
        """ Exception to be thrown if CRC Check failed
        Attributes:
            expression -- input expression in which the error occurred
            message -- explanation of the error
        """
        self.expression = expression
        self.message = message