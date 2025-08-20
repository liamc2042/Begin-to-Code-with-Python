from BTCInput import *

contacts = []

class Contact():
    pass

def new_contact():
    '''
    Reads in a new contact and stores it
    '''
    print('Create new contact')
    #create a new instance
    new_contact=Contact()
    # add the data attributes
    new_contact.name=read_text('Enter the contact name: ')
    new_contact.address=read_text('Enter the contact address: ')
    new_contact.telephone=read_text('Enter the contact phone: ')
    # add the new contact to the contact list
    contacts.append(new_contact)

def find_contact():
    '''
    Reads in a name to search for and then displays
    the contact information for that name or a
    message indicating that the name was not found
    '''
    print('Find contact')
    search_name = read_text('Enter the contact name: ')
    search_name = search_name.strip()
    search_name = search_name.lower()
    # Set result to indicate nothing found
    result=None

    for contact in contacts:
        name=contact.name
        name=name.strip()
        name=name.lower()
        # see whether the names match
        if name.startswitch(search_name):
            #if the names match, set the contact
            result = contact
            # end the loop
            break

    if result != None:
        # Found a name
        print('Name: ', result.name)
        print('Address: ', result.address)
        print('Telephone: ', result.telephone)

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