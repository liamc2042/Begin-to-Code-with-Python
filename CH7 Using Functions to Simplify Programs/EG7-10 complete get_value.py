def get_value(prompt, valMin, valMax):
    while True:
        try:
            num = int(input(prompt))

        except ValueError:
            print('Invalid number text. Please enter digits.')
            continue

        if num < valMin:
            print('Value too small')
            print('The minimum value is', valMin)
            continue

        if num > valMax:
            print('Value too large')
            print('The maximum value is', valMax)
            continue

        return num

def main():
    rideNum = get_value(prompt='Please enter the ride number you want: ', valMin=1, valMax=5)
    print('You have selected ride: ',rideNum)

if __name__ == "__main__":
    main()