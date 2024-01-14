import re
import os
import fitz
from glob import glob

pdf_filenames = glob(os.path.join('./pdfs/', '*.pdf'))
extracted_text = ""

def get_re_matches(regex_str, group_num, input_text):
    # running regex with `/gms`:
    matches = re.finditer(regex_str, input_text, re.MULTILINE | re.DOTALL)

    # going through matches to get certain group:
    matches_final = []
    for match in matches:
        matches_final.append(match.group(group_num).strip())

    return matches_final


## 1. Extract text from PDFs
if (len(pdf_filenames) == 0):
    raise ValueError("Err: No PDF files found in the './pdfs/' directory.")
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

# extraction
tasks        = get_re_matches(r"(^[0-9]{1,}\.\n?\s?)(?![0-9])(.*?)(?=\n?\s\n[A-Z]\.)", 2, extracted_text)
answers      = get_re_matches(r"(^[A-Z]\..*?)(?=\s\n?Odp\.)", 1, extracted_text)
correct      = get_re_matches(r"(?<=^Odp\.)(.*?)([A-Z])(?=\.?)", 2, extracted_text)
explanations = get_re_matches(r"(^Odp\.(\:|\s)\s?[A-Z])(\.?\s+\n?)(.*?)(?=((^[0-9]{1,}\.\n?\s?)(?![0-9]))|(\s\n){3})", 4, extracted_text)

for i in range(len(tasks)):
    print(tasks[i])
    print(answers[i])
    print(correct[i])
    print(explanations[i], '\n')
