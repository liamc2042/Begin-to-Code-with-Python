from BTCInput import *

names=[]
addresses=[]
telephones=[]

def find_contact():
    '''
    Reads in a name to search for and then displays
    the content information for that name or a
    message indicating that the name was not found
    '''

    print('Find contact')
    search_name = read_text('Enter the contact name: ')
    search_name = search_name.strip()
    search_name = search_name.lower()
    name_position=0
    for name in names:
        name=name.strip()
        name=name.lower()
        if name==search_name:
            break
        name_position=name_position+1

    if name_position < len(names):
        print('Name: ', names[name_position])
        print('Address: ', addresses[name_position])
        print('Telephone: ', telephones[name_position])

    else:
        print('This name was not found.')