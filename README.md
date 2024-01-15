# ts-test-extractor

Simple script for extracting questions, answers and so on from test PDFs (for a subject called TS I have at uni) to a more usable format.

**!!!THE REAL TEST PDFS ARE NOT INCLUDED AS I DON'T HAVE THE RIGHT TO PUBLISH THEM!!!**
**!!!KEEP IN MIND THAT THE REGEX PATTERNS AND FORMATTING FIXES IN THIS PROJECT WILL PRETTY MUCH ONLY FIT THIS REALLY SPECIFIC USECASE, THUS IT WILL MOST LIKELY ONLY BE USEFUL AS INSPIRATION!!!

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
