from PyPDF2 import PdfWriter, PdfReader
pdfwriter=PdfWriter()
pdf = PdfReader("e:\\Ashraf\\Wombat Programming\\test.pdf")
for page_num in range(len(pdf.pages)):
  pdfwriter.add_page(pdf.pages[page_num])
passw= input('Enter your password:')
pdfwriter.encrypt(passw)
with open("e:\\Ashraf\\Wombat Programming\\ho.pdf", 'wb') as f:
    pdfwriter.write(f)
