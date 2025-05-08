def main():
    name = input('Enter your name: ')

    if name.upper() == 'LIAM':
        password = input('Enter the password: ')
        if password == 'secret':
            print('Hello, Oh great one')
        else:
            print('Begone. Imposter')

if __name__ == "__main__":
    main()