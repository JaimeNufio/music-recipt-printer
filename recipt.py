from escpos.printer import Usb
import json

class POS_Printer:

  def __init__(self):
    self.VID = ''
    self.PID = ''

    with open('config.json','r') as file:
      data = json.load(file)['printer']

      self.VID = int(data['VID'], 16)
      self.PID = int(data['PID'], 16)


    self.printer = Usb(
      self.VID,
      self.PID,
      0
    )
    self.printer.cut()

  def print(self, path):
    # """ Seiko Epson Corp. Receipt Printer (EPSON TM-T88III) """
    self.printer.image(path)
    self.printer.close()

