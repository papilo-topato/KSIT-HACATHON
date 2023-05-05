import PyPDF2
import PIL
import tkinter as tk
from tkinter import filedialog
import os
#choose PDF file
root = tk.Tk()
root.withdraw()

#select a PDF file
pdf_path = filedialog.askopenfilename(filetypes=[('PDF files', '*.pdf')])
pdf_file = open(pdf_path, 'rb')

#choose operation
print("Choose an operation:")
print("1. Extract text from PDF file using PyPDF2")
print("2. Merge PDF files")
print("3. Split PDF files")
print("4. Get the last page of PDF")
print("5. Rotate PDF")
print("6. Encrypt a PDF file using PyPDF2")

operation = input("Enter operation number: ")

if operation == "1":
    # Extract text from PDF file
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    for page in range(len(pdf_reader.pages)):
        page_obj = pdf_reader.pages[page]
        text = page_obj.extract_text()
        print(text)
elif operation == "2":
    # Merge PDF files
    pdf_merger = PyPDF2.PdfMerger()
    num_pdf = int(input("Enter number of PDFs to merge: "))
    for i in range(num_pdf):
        # choose file to merge
        print(f"Select file {i+1}:")
        file_path = filedialog.askopenfilename(filetypes=[('PDF files', '*.pdf')], parent=tk.Toplevel())
        pdf_merger.append(file_path, 'rb')
    # choose output name
    output_name = filedialog.asksaveasfilename(defaultextension=".pdf")
    with open(output_name, 'wb') as output_file:
        pdf_merger .write(output_file)

elif operation == "3":
    # Split PDF file
    reader = PyPDF2.PdfReader(pdf_file)
    for page in range(len(reader.pages)):
        pdf_writer = PyPDF2.PdfWriter()
        pdf_writer.add_page(reader.pages[page])
        output_name = f"page{page + 1}.pdf"
        with open(output_name, 'wb') as output_file:
            pdf_writer.write(output_file)
elif operation == "4":
    # Get last page of PDF file
    reader = PyPDF2.PdfReader(pdf_file)
    last_page = len(reader.pages) - 1
    print("Last page of PDF file:", last_page)
elif operation == "5":
    # Rotate PDF file
    pdf_writer = PyPDF2.PdfWriter()
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    rotation = int(input("Enter rotation angle: "))
    for page in range(len(pdf_reader.pages)):
        page_obj = pdf_reader.pages[page]
        page_obj.rotate(rotation)
        pdf_writer.add_page(page_obj)
    output_name = input("Enter output PDF file name: ")
    with open(output_name, 'wb') as output_file:
        pdf_writer.write(output_file)
elif operation == "6":
    # Encrypt a PDF file
    pdf_writer = PyPDF2.PdfWriter()
    password = input("Enter password to encrypt PDF: ")
    pdf_writer.encrypt(password)
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    output_name = input("Enter output PDF file name: ")
    for page in range(len(pdf_reader.pages)):
        pdf_writer.add_page(pdf_reader.pages[page])
    with open(output_name, 'wb') as output_file:
        pdf_writer.write(output_file)
