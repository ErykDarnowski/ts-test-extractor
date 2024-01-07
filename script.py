import os
from glob import glob
from PyPDF2 import PdfReader 

pdf_filenames = glob(os.path.join('./pdfs/', '*.pdf'))

with open('out.txt', 'w') as out_file:
    # go through every pdf file
    for filename in pdf_filenames:
        reader = PdfReader(filename)
          
        # go through every page
        for page in reader.pages:
            # save extracted text to output file
            out_file.write(page.extract_text()
                           .replace(' ą', 'ą')
                           .replace(' ę', 'ę')
                           .replace(' ń', 'ń')
                           .replace(' ś', 'ś')
                           .replace('Ŝ', 'ż'))
                           # ^ fixes issue with Polish diacritic characters
                           # uppercase characters are not done as I couldn't
                           # find any issues with them as of now
