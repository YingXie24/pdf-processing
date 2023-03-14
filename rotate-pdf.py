import PyPDF2

with open('dummy.pdf', 'rb') as file:
    # initialise a PdfFileReader object
    reader = PyPDF2.PdfFileReader(file)

    # retrieve the first page from this PDF file
    # returns a page object
    page = reader.getPage(0)

    # rotate the page object
    page.rotateClockwise(90)

    # initialise PdfFileWriter object
    writer = PyPDF2.PdfFileWriter()

    # add a page to this object
    writer.addPage(page)

    # write the object out as a PDF file
    with open('rotated.pdf', 'wb') as new_file:
        writer.write(new_file)

