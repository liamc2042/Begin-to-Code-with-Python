def main():
    while True:
        try:
            rideNum = int(input('Please enter the ride number you want: '))
            break
        except ValueError:
            print('Invalid entry. Please enter digits')

    print('You have selected ride', rideNum)
if __name__ == "__main__":
    main()