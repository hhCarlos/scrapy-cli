# 🕷️ scrapy-cli

A simple CLI tool for web scraping using Python.

## Features
- Input any URL from console.
- Define selectors by class or ID.
- Display matched HTML elements.
- Save output to CSV/JSON (coming soon).

## Run
```bash
pip install -r requirements.txt
python src/main.py

## Utilities

Command to eleminate cache from test:
- find . -type d -name "__pycache__" -exec rm -r {} +
