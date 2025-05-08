import time

def main():
    currTime = time.localtime()
    hour = currTime.tm_hour
    minute = currTime.tm_min

    if (hour>7) or (hour==7 and minute>29):
        print('IT IS TIME TO GET UP')
        print('RISE AND SHINE')
        print('THE EARLY BIRD GETS THE WORM')
    print('The time is', hour,':',minute)

if __name__ == "__main__":
    main()