import qrcode as qr
img = qr.make("https://www.youtube.com/@CodeWithHarry")
img.save("harry_youtube.png")
