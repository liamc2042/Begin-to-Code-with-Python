def main():
    print('''Welcome to our Theme Park
            
          These are the available rides:
          
          1. Scenic River Cruise
          2. Carnival Carousel
          3. Jungle Adventure Water Splash
          4. Downhill Mountain Run
          5. The Regurgitator
          ''')
    
    rideNum = int(input('Please enter the ride number you want: '))

    if rideNum == 1:
        print('You have selected the Scenic River Cruise')
        print('There is no age limits for this ride')

    else:
        age = int(input('Please enter your age: '))

    if rideNum == 2:
        print('You have selected the Carnival Carousel')
        if age >= 3:
            print('You can go on the ride')
        else:
            print('Sorry, you are too young.')

    if rideNum == 3:
        print('You have selected the Jungle Adventure Water Splash')
        if age >= 6:
            print('You can go on the ride')
        else:
            print('Sorry, you are too young.')

    if rideNum == 4:
        print('You have selected the Downhill Mountain Run')
        if age >= 12:
            print('You can go on the ride')
        else:
            print('Sorry, you are too young.')

    if rideNum == 5:
        print('You have selected The Regurgitator')
        if age >= 12:
            if age > 70:
                # Age too old
                print('Sorry, you are too old')
            else:
                print('You can go on the ride')

        else:
            # Age too young
            print('Sorry, you are too young.')

if __name__ == "__main__":
    main()