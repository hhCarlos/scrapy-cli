from menus.main_menu import handle_selection, show_menu


def main():
  running = True
  while running:
    show_menu()
    option = input("Select an option (1-3): ")
    running = handle_selection(option)


if __name__ == "__main__":
  main()
