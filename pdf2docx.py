from pdf2docx import Converter


pdf_file = 'input.pdf'
docx_file = 'input_2.docx'


cv= Converter(pdf_file)
cv.convert(docx_file)
cv.close()