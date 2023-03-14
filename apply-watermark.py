import PyPDF2

# initialise watermark, template and output objects
watermark = PyPDF2.PdfFileReader('wtr.pdf')
template = PyPDF2.PdfFileReader('twopage.pdf')
output = PyPDF2.PdfFileWriter()

# determine the number of pages in the template
num_pages = template.getNumPages()

# loop through all pages in template
for i in range(num_pages):
    page = template.getPage(i)
    print('reading page', page)

    # add watermark to the page
    page.mergePage(watermark.getPage(0))

    # add watermarked page to output object
    output.addPage(page)

    # write the object out as a PDF file
    with open('watermarked.pdf', 'wb') as new_file:
        output.write(new_file)