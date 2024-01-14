import re
import os
import fitz
from glob import glob

pdf_filenames = glob(os.path.join('./pdfs/', '*.pdf'))
extracted_text = ""


## 1. Extract text from PDFs
# go through every pdf file
for filename in pdf_filenames:
    # open document
    with fitz.open(filename) as pdf_file:
        # iterate through every page
        for page in pdf_file:
            # save plain text encoded as UTF-8
            extracted_text += page.get_text().replace('Ŝ', 'ż')

## 2. Get tasks, answers and so on via regex patterns
# clean up (removes page titles - fix for bug with `tasks` regex)
extracted_text = re.sub(r"(\s\n){0,2}(^Test\sz\s.*?)(\s\n){2,}", "", extracted_text, 0, re.MULTILINE | re.DOTALL)

print(extracted_text)
