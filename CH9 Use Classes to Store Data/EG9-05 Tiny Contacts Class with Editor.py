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

def find_contact(search_name):
    '''
    Finds the contact with the matching name
    Returns a contact instance or None if there is
    no contact with the given name
    '''
    search_name = search_name.strip()
    search_name = search_name.lower()
    # Set result to indicate nothing found
    for contact in contacts:
        name=contact.name
        name=name.strip()
        name=name.lower()
        # see whether the names match
        if name.startswitch(search_name):
            #if contact is found, return contact
            return contact
        
    return None

def display_contact():
    '''
    Reads in a name to search for and then displays
    the content information for that name or a 
    message indicating that the name was not found
    '''
    print('Find contact')
    search_name = read_text('Enter the contact name: ')
    contact = find_contact(search_name)
    if contact != None:
        print('Name: ', contact.name)
        print('Address: ', contact.address)
        print('Telephone: ', contact.telephone)

    else:
        print('This name was not found. ')

def edit_contact():
    '''
    Reads in a name to search for and then allows
    the user to edit details of that contact.
    If there is no contact, the function displays a
    message indicating that the name was not found
    '''
    print('Edit contact')
    search_name=read_text('Enter the contact name: ')
    contact=find_contact(search_name)
    if contact!=None:
        # found contact
        print('Name: ', contact.name)
        new_name=read_text('Enter new name or . to leave unchanged: ')
        if new_name!='.':
            contact.name=new_name
        new_address=read_text('Enter new address or . to leave unchanged: ')
        if new_address!='.':
            contact.address=new_address
        new_phone=read_text('Enter new telephone or . to leave unchanged: ')
        if new_phone!='.':
            contact.telephone=new_phone

    else:
        print('This name was not found.')

def main():
    menu= '''Tiny Contacts
    
    1. New Contact
    2. Find Contact
    3. Edit Contact
    4. Exit Program
    
    Enter you command: '''

    while True:
        command=read_int_ranged(prompt=menu, min_value=1, max_value=4)
        if command == 1:
            new_contact()
        elif command == 2:
            display_contact()
        elif command == 3:
            edit_contact()
        elif command == 4:
            break

if __name__ == '__main__':
    main()