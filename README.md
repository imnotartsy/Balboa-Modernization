# Balboa-Modernization
A program that reads scanned documents using Google Cloud's OCR technology and imports it into an organized spreadsheet.

Logs and Documentation: https://docs.google.com/document/d/1dr1je4OwtGZ-50fQA4Ms04PabwQGlvT2EpihO-oXXhY/edit?usp=sharing

# Getting Started
- The inital code is from 
https://cloud.google.com/vision/docs/ocr?apix_params=%7B%22resource%22%3A%7B% 7D%7D#vision_text_detection-python

- The initial Google Cloud Auth .json is not being included on this public repo. Steps to get started are here: https://cloud.google.com/vision/docs/quickstart-client-libraries

- Do not forget to run 
```export GOOGLE_APPLICATION_CREDENTIALS="[PATH]"```
and ```pip install --upgrade google-cloud-vision``` (in the link above)
