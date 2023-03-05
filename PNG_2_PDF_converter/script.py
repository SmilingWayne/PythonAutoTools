from fpdf import FPDF
import os
pdf = FPDF()
png_list = []

for filename in os.listdir("./PNGs"):
    if filename.endswith('.png'):
        png_list.append(os.path.join("./PNGs", filename))

png_list.sort()

for link in png_list:
    # set image dimensions
    pdf.add_page()
    width = 210
    height = 297
    pdf.image(link, x=0, y=0, w=width, h=height)

pdf.output('./Result/output.pdf', 'F')
