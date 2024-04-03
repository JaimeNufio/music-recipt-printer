from escpos import printer
import json
import serial
import time

class POS_Printer:

  def __init__(self):
    self.VID = ''
    self.PID = ''

    with open('config.json','r') as file:
      data = json.load(file)['printer']

      self.VID = bytes.fromhex(data['VID'])
      self.PID = bytes.fromhex(data['PID'])

    print(self.VID,self.PID)

    self.printer = printer.Usb(
      self.VID,
      self.PID,
      0
    )
    # self.printer = printer.Serial('COM1')

    self.printer.cut()

  def print(self, path):
    # """ Seiko Epson Corp. Receipt Printer (EPSON TM-T88III) """
    self.printer.image(path)
    self.printer.close()

