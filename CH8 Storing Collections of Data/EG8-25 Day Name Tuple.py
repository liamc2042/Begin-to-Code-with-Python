from BTCInput import *

def main():
    day_number=1

    day_names=('Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday')
    
    day_name=day_names[day_number]
    
    # this statement will raise an exception because
    # a tuple is immutable (cannot be changed)
    day_names[5]='Splatterday'
    
    print(day_name)

if __name__ == '__main__':
    main()