import sys
import os

# Force Python to see directory: src/
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

from utils.validators import is_valid_url


def test_valid_url_returns_true():
    assert is_valid_url("https://www.google.com") is True


def test_invalid_url_returns_false():
    assert is_valid_url("not-a-url") is False


def test_non_string_input_returns_false(capfd):
    result = is_valid_url(12345)
    out, _ = capfd.readouterr()
    assert result is False
    assert "tipo de dato" in out
