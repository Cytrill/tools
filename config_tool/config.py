#!/usr/bin/env python2
from PyQt4 import QtGui, QtCore
import sys
import os
import time
import serial

import config_ui

class CytrillDevice(object):
    def __init__(self, port):
        self.device = serial.Serial(port=port, baudrate=115200)
        self.device.close()
        self.device.open()

    def reset_to_app(self):
        self.device.setDTR(False)
        self.device.setRTS(True)
        time.sleep(0.005)
        self.device.setRTS(False)

    def set_wireless_config(self, essid, password):
        self.device.write(bytes(essid + "\n"))
        self.device.write(bytes(password + "\n"))

    def close():
        self.device.close()

class CytrillConfigWindow(QtGui.QDialog, config_ui.Ui_frmCytrillConfig):
    POSSIBLE_PORTS = [ "/dev/ttyUSB0",
                       "/dev/ttyUSB1",
                       "/dev/ttyUSB2",
                       "/dev/ttyUSB3",
                       "/dev/ttyACM0",
                       "/dev/ttyACM1",
                       "/dev/ttyACM2",
                       "/dev/ttyACM3" ]
    def __init__(self):
        super(self.__class__, self).__init__()

        self.setupUi(self)
        self.btnWriteConfig.clicked.connect(self.write_config)

    def write_config(self):
        self.ctrl = None

        for port in self.POSSIBLE_PORTS:
            if os.path.isfile(port):
                self.ctrl = CytrillDevice(port)
                break
        else:
            self.lblStatus.setText("No serial port found!")

        if self.ctrl != None:
            essid = self.leESSID.text()
            password = self.lePassword.text()

            self.lblStatus.setText("Resetting device...")
            self.ctrl.reset_to_app()
            QtCore.QTimer.singleShot(2000, lambda: self.lblStatus.setText("Writing new config..."))
            QtCore.QTimer.singleShot(2000, lambda: self.ctrl.set_wireless_config(essid, password))
            QtCore.QTimer.singleShot(3000, lambda: self.ctrl.reset_to_app())
            QtCore.QTimer.singleShot(5000, lambda: self.lblStatus.setText("Finished!"))

            self.ctrl.close()

def main():
    app = QtGui.QApplication(sys.argv)
    form = CytrillConfigWindow()
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()
