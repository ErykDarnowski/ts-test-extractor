# ts-test-extractor

Simple script for extracting questions, answers and so on from test PDFs (for a subject called TS I have at uni) to a more usable format.

\***The real test pdfs are not included as i don't have the right to publish them!**\
\***Keep in mind that the regex patterns and formatting fixes in this project will pretty much only fit this really specific usecase, thus it will most likely only be useful as inspiration!**

## Setup

- Unix
	```bash
	# 1. Create virtual env:
	python3 -m venv venv
	
	# 2. Activate virtual env:
	source venv/bin/activate 
	
	# 3. Install required pkgs:
	pip install -r requirements.txt
	```
- Windows
	```bash
	# 1. Create virtual env:
	python3 -m venv venv
	
	# 2. Activate virtual env:
	.\venv\Scripts\activate 
	
	# 3. Install required pkgs:
	pip install -r requirements.txt
	```

## Instructions

1. Place the test PDFs files in the `./pdfs/` directory (for best results they should be numbered) - an example MS Word document and it's PDF export are included
2. After performing the **Setup** step, simply run: `python3 script.py`
3. Use the output JSON file (`ts.json`) however you see fit
