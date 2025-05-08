import snaps

def main():
    name = snaps.get_string('Enter your name: ')
    snaps.display_message('Hello' + name)

if __name__ == "__main__":
    main()