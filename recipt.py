from escpos.printer import Usb
from PIL import Image 

image = Image.open("a.jpeg")

# Resize the image to 512x512
resized_image = image.resize((512, 512))

# Save the resized image
resized_image.save("b.jpg")

# """ Seiko Epson Corp. Receipt Printer (EPSON TM-T88III) """
p = Usb(0x04b8, 0x0202, 0, profile="TM-T88III")
p.text("-----\n")
p.image('album.jpeg')
p.text("12345678901234567890123456789012\n")
p.text("----\n")
# Cut the paper
p.cut()

# # Close the connection
# p.close()

# # p.cut()

# print(len("12345678901234567890123456789012"))