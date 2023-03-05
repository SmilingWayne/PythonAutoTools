import os
from PyPDF2 import PdfFileMerger

# Specify the folder path where the PDF files are located
folder_path = './PDFs'

# Create an empty PDF merger object
pdf_merger = PdfFileMerger()

# Iterate through all the PDF files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith('.pdf'):
        # Open each PDF file in read-binary mode and add it to the merger object
        with open(os.path.join(folder_path, filename), 'rb') as pdf_file:
            pdf_merger.append(pdf_file)

# Write the merged PDF to a new file
with open('merged.pdf', 'wb') as output:
    pdf_merger.write(output)
