def main():
    rideNumValid = False
    while not rideNumValid:
        try:
            rideNum = int(input('Please enter the ride number you want: '))
            rideNumValid = True
        except ValueError:
            print('Invalid number. Please enter digits.')
        except KeyboardInterrupt:
            print('Please do not try to stop the program.')

    print('You have selected ride', rideNum)
if __name__ == "__main__":
    main()