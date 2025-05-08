import time

def main():
    timeText = input('Enter the cooking time in seconds: ')
    intTime = int(timeText)
    print('Put the egg in boiling water now')

    time.sleep(intTime)

    print('Take the egg out now')

if __name__ == "__main__":
    main()