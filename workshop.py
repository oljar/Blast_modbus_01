def settings_6(self):
    self.instrument_6 = minimalmodbus.Instrument("/dev/ttyUSB0", self.model.dev_6_adr_var)
    # self.instrument_6 = minimalmodbus.Instrument('com4', self.model.dev_6_adr_var)
    self.instrument_6.serial.baudrate = 9600  # Baud
    self.instrument_6.serial.bytesize = 8
    self.instrument_6.serial.parity = serial.PARITY_NONE
    self.instrument_6.serial.stopbits = 1
    self.instrument_6.serial.timeout = 0.5  # seconds
    self.instrument_6.address = 16  # this is the slave address number
    self.instrument_6.mode = minimalmodbus.MODE_RTU  # rtu or ascii mode