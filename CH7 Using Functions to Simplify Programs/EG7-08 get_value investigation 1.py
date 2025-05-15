def get_value(prompt, valMin, valMax):
    return 1
    return 2

def main():
    rideNum = get_value(prompt='Please enter the ride number you want: ', valMin=1, valMax=5)
    print('You have selected ride: ',rideNum)

if __name__ == "__main__":
    main()