def main():
    while True:
        rideNum = int(input('Please enter the ride number you want: '))
        if rideNum == 3:
            print('Sorry, this ride is not available')
            continue
        print('You have selected ride number: ',rideNum)
if __name__ == "__main__":
    main()