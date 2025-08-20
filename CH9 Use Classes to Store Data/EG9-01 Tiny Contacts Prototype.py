from BTCInput import *

def new_contact():
    print('Create new contact')
    read_text('Enter the contact name: ')
    read_text('Enter contact address: ')
    read_text('Enter contact phone: ')

def find_contact():
    print('Find contact')
    name = read_text('Enter the contact name: ')
    if name == 'Rob Miles':
        print('Name: Rob Miles')
        print('Address: 18 Pussycat Mews, London, NE1 410S')
        print('Phone: +44(1234) 56789')
    else:
        print('This name was not found')

def main():
    menu= '''Tiny Contacts
    
    1. New Contact
    2. Find Contact
    3. Exit Program
    
    Enter you command: '''

    while True:
        command=read_int_ranged(prompt=menu, min_value=1, max_value=3)
        if command == 1:
            new_contact()
        elif command == 2:
            find_contact()
        elif command==3:
            break

if __name__ == '__main__':
    main()