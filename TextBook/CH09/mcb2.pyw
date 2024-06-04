import shelve, pyperclip, sys

def main():
    mcb_shelf = shelve.open('mcb')

    if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
        mcb_shelf[sys.argv[2]] = pyperclip.paste()
    elif len(sys.argv) == 2:
        if sys.argv[1].lower() == 'list':
            pyperclip.copy(str(list(mcb_shelf.keys())))
        elif sys.argv[1] in mcb_shelf:
            pyperclip.copy(mcb_shelf[sys.argv[1]])
    elif len(sys.argv) == 3 and sys.argv[1].lower() == 'delete':
        if sys.argv[2] in mcb_shelf:
            del mcb_shelf[sys.argv[2]]
            print(f"Deleted {sys.argv[2]} from the shelf.")
        else:
            print(f"{sys.argv[2]} not found in the shelf.")
    elif len(sys.argv) == 2 and sys.argv[1].lower() == 'delete':
        mcb_shelf.clear()
        print("All entries deleted from the shelf.")

    mcb_shelf.close()

if __name__ == "__main__":
    main()

