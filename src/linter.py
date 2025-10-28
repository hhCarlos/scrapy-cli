import subprocess
import sys


def run_linter():
  print("🚀 Running flake8 linting...\n")
  try:
      result = subprocess.run(
        ["flake8", "src", "--count", "--show-source", "--statistics"],
        check=True,
      )
      print("\n✅ Lint passed successfully.")
      return result.returncode
  except subprocess.CalledProcessError as e:
      print("\n❌ Linting failed with errors.")
      return e.returncode
  except FileNotFoundError:
      print("⚠️ Flake8 not found. Make sure it's installed and listed in requirements.txt.")
      return 1


if __name__ == "__main__":
  sys.exit(run_linter())
