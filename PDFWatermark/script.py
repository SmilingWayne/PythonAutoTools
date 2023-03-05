import os
import PyPDF2

# Set the input folder path and watermark file path
input_folder = 'PDF/'  # The pdf you want to modify
watermark_file = './Watermark/WaterMark.pdf'  # The watermark pdf

# Create a PDF reader object for the watermark file
with open(watermark_file, 'rb') as watermark_file:
    watermark_reader = PyPDF2.PdfFileReader(watermark_file)
    watermark_page = watermark_reader.getPage(0)

    # Loop through all PDF files in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith('.pdf'):
            # Open the input PDF file in read-binary mode
            with open(os.path.join(input_folder, filename), 'rb') as pdf_file:
                # Read the PDF content
                pdf_reader = PyPDF2.PdfReader(pdf_file)

                # Create a PDF writer object
                pdf_writer = PyPDF2.PdfWriter()

                # Add the watermark to each page of the input PDF file
                for page_num in range(len(pdf_reader.pages)):
                    page = pdf_reader.pages[page_num]
                    page.merge_page(watermark_page)
                    pdf_writer.add_page(page)

                # Write the output PDF file with watermark
                with open(os.path.join(input_folder, 'watermarked_' + filename), 'wb') as output_file:
                    pdf_writer.write(output_file)
