import fitz  # PyMuPDF
import os

def pdf_to_jpg(pdf_path, output_folder):
    # Ensure the output folder exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Open the provided PDF
    doc = fitz.open(pdf_path)
    
    for page_num in range(len(doc)):
        # Get the page
        page = doc.load_page(page_num)
        
        # Get the Pixmap of the page (raster image)
        pix = page.get_pixmap()
        
        # Define the output image path
        output_image_path = f"{output_folder}/page_{page_num + 1}.jpg"
        
        # Save the pixmap (image) to a file
        pix.save(output_image_path)
        
    print(f"Conversion completed. Extracted {len(doc)} pages.")

# Assuming the Python script and 'test.pdf' are both in the 'share' folder
pdf_path = "test.pdf"
output_folder = "./output_images"

# Adjust the output folder path to the full path as needed
pdf_to_jpg(pdf_path, output_folder)