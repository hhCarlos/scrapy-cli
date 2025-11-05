import requests
import re
from bs4 import BeautifulSoup
from typing import List, Optional


class Scraper:
  def __init__(self, url: str):
    print(f"Starting scrape on: {url}")
    self.url = url
    self.selectors: List[str] = []
    self.html_content: Optional[str] = None
    self.soup: Optional[BeautifulSoup] = None

  def start(self):
    """Main entry point for scrapper process"""
    self.collect_selectors()

  def collect_selectors(self):
    """Interactively collect CSS selectors from user."""
    print("Add selectors one by one. Type 'n' or 'N' to finish.\n")

    try:
      while True:
        selector = input('Selector:').strip()
        if selector.lower() == 'n':
          break
        if not selector:
          print("Empty selector ignored.")
          continue
        if not self.validate_selector(selector):
          print(f"El selector: {selector} no es valido.")
          continue
        self.selectors.append(selector)
      print(f"✅ Selectors collected: {self.selectors}")
      self.fetch_html()
    except KeyboardInterrupt:
      print("Proccess interrupted by user.")
      exit(0)

  def fetch_html(self):
    """Fetch HTML content from url."""
    print("Fetching HTML content...")
    try:
      response = requests.get(self.url)
      response.raise_for_status()
      self.html_content = response.text
      self.soup = BeautifulSoup(self.html_content, "html.parser")
      print("Page loaded successfully.")
      self.parse_selectors()
    except requests.RequestException as e:
      print(f"Failed to fetch url: {e}")
      exit(1)

  def parse_selectors(self):
    """Parse the collected selector using BeautifulSoup."""
    if not self.soup:
      print("No HTML content loaded. Run fetch_html() first.")
      return

    for selector in self.selectors:
      print(f"Searching for selector: {selector}")
      elements = self.soup.select(selector)
      print(f"Found {len((elements))}.\n")

  def validate_selector(self, selector: str) -> bool:
    pattern = r"^([a-zA-Z][\w\-]*|\.[\w\-]+|#[\w\-]+)$"
    return bool(re.match(pattern, selector))
