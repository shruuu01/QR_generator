import qrcode
from PIL import Image
qr = qrcode.QRCode(version=1,
                   error_correction = qrcode.constants.ERROR_CORRECT_H,
                   box_size=10,border=10,)
qr.add_data("https://@CodeWithHarry")
qr.make(fit=True)
img = qr.make_image( fill_color="green", back_color="white")
img.save("harry_web.png")