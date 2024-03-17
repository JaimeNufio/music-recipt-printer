from escpos.printer import Usb

class POS_Printer:

  def __init__(self):
    self.printer = Usb(0x04b8, 0x0202, 0, profile="TM-T88III")
    self.printer.cut()

  def print(self, path):
    # """ Seiko Epson Corp. Receipt Printer (EPSON TM-T88III) """
    self.printer.image(path)
    self.printer.close()

