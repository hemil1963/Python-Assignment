''' ID:-20CS063    NAME:Hemil Patoliya'''
'''Aim:-Generate PDF file of your 3rd Semester Mark-sheet'''

import img2pdf

from PIL import Image

import os


img_path = "20cs063_sem3.png"
pdf_path = "20cs063_sem3.pdf"

# opening image
image = Image.open(img_path)
# converting into chunks using img2pdf
pdf_bytes = img2pdf.convert(image.filename)

# opening or creating pdf file
file = open(pdf_path, "wb")
# writing pdf files with chunks
file.write(pdf_bytes)
# closing image file
image.close()

# closing pdf file
file.close()
