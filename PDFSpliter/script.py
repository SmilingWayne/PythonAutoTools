from PyPDF2 import PdfWriter, PdfReader
import os
from PyPDF2 import PdfReader, PdfWriter


input_folder = './Target'
output_folder = './Result'

# iterate through all PDF files in input folder
for filename in os.listdir(input_folder):
    if filename.endswith('.pdf'):
        # open input PDF
        input_path = os.path.join(input_folder, filename)
        pdf_reader = PdfReader(input_path)

        # get number of pages in input PDF
        try:
            num_pages = len(pdf_reader.pages)

            # set maximum number of pages per output PDF
            max_pages_per_pdf = 4

            # split input PDF into multiple output PDFs
            for i in range(0, num_pages, max_pages_per_pdf):
                # create output PDF
                output_path = os.path.join(
                    output_folder, f'{filename}_{i+1}-{min(i+max_pages_per_pdf, num_pages)}.pdf')
                pdf_writer = PdfWriter()

                # add pages to output PDF
                for j in range(i, min(i+max_pages_per_pdf, num_pages)):
                    page = pdf_reader.pages[j]
                    pdf_writer.add_page(page)

                # write output PDF
                with open(output_path, 'wb') as output_file:
                    pdf_writer.write(output_file)
        except Exception:
            print(filename + " Not fine!")
