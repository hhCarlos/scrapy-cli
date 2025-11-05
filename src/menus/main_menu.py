def show_menu():
  print("\n=== Scrapy-CLI ===")
  print("1. Find elements fast with CLI-version.")
  print("2. Find elements in browser and interact with them.")
  print("3. Exit app.")


def handle_selection(option: str):
  if option == "1":
    print("Corre el cli version...")
  elif option == "2":
    print("Corre la version browser...")
  elif option == "3":
    print("Exiting Scrapy-CLI: Comeback any time!")
    return False
  else:
    print("Invalid option, try again!")
  return True
