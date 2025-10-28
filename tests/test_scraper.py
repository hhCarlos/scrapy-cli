import sys
import os

# Force Python to see directory: src/
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

from scraper import start_scraper


def test_start_scraper_output(capfd):
    """Should print the correct starting message."""
    url = "https://example.com"
    start_scraper(url)
    out, _ = capfd.readouterr()
    assert f"Starting scrape on: {url}" in out
