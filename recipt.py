from escpos.printer import Usb
from win32 import win32print
import usb.core
import json
import serial
import time

class POS_Printer:

  def seek_device(self, VID,PID):
    dev = usb.core.find(idVendor=VID,idProduct=PID)

    if dev is None:
      raise ValueError('Device not found!')
      return False
    else:
      return True


  def __init__(self):
    self.VID = ''
    self.PID = ''

    with open('config.json','r') as file:
      data = json.load(file)['printer']

      self.VID = (int(data['VID'],16))
      self.PID = (int(data['PID'],16))

    print(self.VID,self.PID)

    if (not self.seek_device(self.VID,self.PID)):
      print("Won't init, can't find device.")
      return

    self.printer = Usb(
      self.VID,
      self.PID,
      0 ,
      profile='TM-T88V'
    )

    self.printer.cut()

  def print(self, path):
    self.printer.image(path)
    # self.printer.close()

