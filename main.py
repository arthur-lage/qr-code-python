import qrcode

stringToQRCode = str(input("Type the text/url that you want to use in your QR Code: "))

img = qrcode.make(stringToQRCode)
img.save("qrcode.png")