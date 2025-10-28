from utils.validators import is_valid_url
from scraper import start_scraper


def main():
  try:
    url = input("Enter a URL: ").strip()
    if not is_valid_url(url):
      print("Invalid URL. Exiting...")
      return
    print(f"URL accepted: {url}")
    start_scraper(url)
  except KeyboardInterrupt:
    print("Process interrupted. Exiting...")


if __name__ == "__mian__":
  main()
