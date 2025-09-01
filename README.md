# Excel Translation Tool

A web application built with Streamlit that translates Excel files into multiple languages using Google Translate.

## Features

- Upload Excel (.xlsx) files
- Translate content to multiple languages (German, French, Spanish, Italian, Chinese, Japanese, Polish)
- Download translated files as Excel format
- Side-by-side comparison of original and translated content

## How to Use

1. Upload your Excel file using the file uploader
2. Select target language(s) from the dropdown
3. View the translated content in the app
4. Download the translated Excel file

## Languages Supported

- German (de)
- French (fr)
- Spanish (es)
- Italian (it)
- Chinese (zh)
- Japanese (ja)
- Polish (pl)

## Deployment

This app is deployed on Streamlit Community Cloud.

## Local Development

To run locally:

```bash
pip install -r requirements.txt
streamlit run ocr2.py
```

## Dependencies

- pandas: For Excel file handling
- deep-translator: For translation functionality
- streamlit: For web interface
- openpyxl: For reading Excel files
- xlsxwriter: For writing Excel files
