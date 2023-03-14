import PyPDF2
import sys

user_input = sys.argv[1:]


def pdf_merger(pdf_list):
    # initialise PdfFileMerger object
    merger = PyPDF2.PdfFileMerger()

    # add pdfs to the end of file
    for pdf in pdf_list:
        merger.append(pdf)

    # write merged data to an output file
    merger.write('merged-pdf.pdf')


pdf_merger(user_input)
