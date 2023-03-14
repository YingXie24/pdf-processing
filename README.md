# pdf-processing

This folder contains three scripts that processes pdf files:
1. rotate-pdf.py
2. merge-pdf.py
3. apply-watermark.py

The library PyPDF2 1.27.12 is used.

Two PDF files, `dummy.pdf` and `twopage.pdf` are provided for manipulation.

To run merge-pdf.py, the command line is needed, with the pdfs-to-combine as arguments. For example:
`python merge-pdf.py dummy.pdf twopage.pdf`
