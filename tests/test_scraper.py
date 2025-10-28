import sys
import os

# ✅ Ensure Python can import from src/
CURRENT_DIR = os.path.dirname(__file__)
SRC_PATH = os.path.abspath(os.path.join(CURRENT_DIR, "../src"))
if SRC_PATH not in sys.path:
    sys.path.insert(0, SRC_PATH)

from scraper import Scraper


def test_scraper_initial_state():
    """Should initialize with correct URL and empty selectors list."""
    url = "https://example.com"
    scraper = Scraper(url)

    # Verifica estado inicial
    assert scraper.url == url
    assert scraper.selectors == []
