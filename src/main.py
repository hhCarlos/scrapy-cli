from utils.validators import is_valid_url
from scraper import Scraper


def main():
  url = input("Enter a valid URL: ").strip()
  if not is_valid_url(url):
    print("Invalid url. Exiting...")
    return

  scraper = Scraper(url)
  scraper.start()


if __name__ == "__main__":
  main()
