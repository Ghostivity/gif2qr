import segno
from urllib.request import urlopen

text = input("Text or URL: ")
qr = segno.make_qr(text)
URL = input('gif url: ')
scale = input("scale: ")
filename = input("filename: ")
gif_qr = urlopen(URL)
qr.to_artistic(
	background=gif_qr,
	target=filename + ".gif",
	scale=scale,
	border=0
	
)
