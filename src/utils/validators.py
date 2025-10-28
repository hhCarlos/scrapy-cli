from urllib.parse import urlparse


def is_valid_url(url: str) -> bool:
  """Check if a given string is a valid url"""
  if not isinstance(url, str):
    print('Validators: El tipo de dato es incorrecto')
    return False

  parsed = urlparse(url)
  return all([parsed.scheme, parsed.netloc])
