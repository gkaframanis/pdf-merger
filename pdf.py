"""
    PDF Merger
"""

import PyPDF2
from sys import argv

# To grab all the arguments from the argument to the 1 position till the last.
inputs = argv[1:]

def pdf_combiner(pdf_list):
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdf_list:
        merger.append(pdf)
    merger.write("merged.pdf")

pdf_combiner(inputs)