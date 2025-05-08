import time

def main():
    currTime = time.localtime()
    hour = currTime.tm_hour
    print('The hour is', hour)

if __name__ == "__main__":
    main()