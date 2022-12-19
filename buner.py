import os
import png 
import pyqrcode
from pyqrcode import QRCode
b = """\033[1;92m
 ▄▄▄▄▄▄▄  ▄ ▄▄ ▄▄▄▄▄▄▄
 █ ▄▄▄ █ ██ ▀▄ █ ▄▄▄ █
 █ ███ █ ▄▀ ▀▄ █ ███ █
 █▄▄▄▄▄█ █ ▄▀█ █▄▄▄▄▄█
 ▄▄ ▄  ▄▄▀██▀▀ ▄▄▄ ▄▄
 ▄██ ▀ ▄ █▄▀ ▄ ▄█▀▀  ▄  
 █▀█▄▄█▄ ▀▀▄▀▄▄▀ ▀▀▄ █    
 ▄▄▄▄▄▄▄ █ ▄▀  ▄█▄▄██       
 █ ▄▄▄ █  ▄▄█▀█▄ ▀ ▄▄
 █ ███ █ ▀▀█▀▄  ██ ▀▀█
 █▄▄▄▄▄█ █▀ ▄▄▀▀ █▄ ▄

"""
print (b)
def cod():
	code = input('\033[1;37mselect QR : ')
	QR = pyqrcode.create(code)
	QR.png("QRcode.png",scale=6)
	os.system("rm static/QRcode.png")
	os.system("mv QRcode.png static")
for i in range(0,100):
	cod()
