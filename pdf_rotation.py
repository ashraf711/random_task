import PyPDF2

def rotate_pdf(input_pdf_path, output_pdf_path):
    # Open the input PDF file
    with open(input_pdf_path, 'rb') as input_file:
        pdf_reader = PyPDF2.PdfReader(input_file)
        pdf_writer = PyPDF2.PdfWriter()

        # Rotate each page
        for page in pdf_reader.pages:
            # Updated to use the `rotate` method
            page.rotate(180)  # Rotating the page by 180 degrees
            pdf_writer.add_page(page)

        # Save the output PDF
        with open(output_pdf_path, 'wb') as output_file:
            pdf_writer.write(output_file)

if __name__ == "__main__":
    input_pdf_path = 'test.pdf'  # Path for the input PDF
    output_pdf_path = 'test_rotated.pdf'  # Path for the output PDF

    rotate_pdf(input_pdf_path, output_pdf_path)