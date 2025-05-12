def main():

    try:
        rideNum = int(input('Please enter the ride number you want: '))
        print('You have entered', rideNum)

    except ValueError:
        print('Invalid number')

if __name__ == "__main__":
    main()