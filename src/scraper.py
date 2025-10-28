from typing import List


class Scraper:
  def __init__(self, url: str):
    print(f"Starting scrape on: {url}")
    self.url = url
    self.selectors: List[str] = []

  def start(self):
    """Main entry point for scrapper process"""
    self.collect_selectors()
    print(f"✅ Selectors collected: {self.selectors}")
    

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
        self.selectors.append(selector)
    except KeyboardInterrupt:
      print("Proccess interrupted by user.")
      exit(0)
