import os
import fitz
from glob import glob

pdf_filenames = glob(os.path.join('./pdfs/', '*.pdf'))

with open('out.txt', 'w', encoding="utf-8") as out_file:
    # go through every pdf file
    for filename in pdf_filenames:
        # open document
        with fitz.open(filename) as pdf_file:
            # iterate through every page
            for page in pdf_file:
                # save plain text encoded as UTF-8
                out_file.write(page.get_text().replace('Ŝ', 'ż'))
