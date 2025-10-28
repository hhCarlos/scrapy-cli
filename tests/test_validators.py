import sys
import os

# ✅ Ensure Python can import from src/
CURRENT_DIR = os.path.dirname(__file__)
SRC_PATH = os.path.abspath(os.path.join(CURRENT_DIR, "../src"))
if SRC_PATH not in sys.path:
    sys.path.insert(0, SRC_PATH)

from utils.validators import is_valid_url


def test_valid_url_returns_true():
    """Should return True for a valid URL."""
    assert is_valid_url("https://www.google.com") is True


def test_invalid_url_returns_false():
    """Should return False for an invalid URL."""
    assert is_valid_url("not-a-url") is False


def test_non_string_input_returns_false(capfd):
    """Should handle non-string inputs gracefully and print warning."""
    result = is_valid_url(12345)
    out, _ = capfd.readouterr()
    assert result is False
    assert "tipo de dato" in out.lower()
