import time

def main():
    currTime = time.localtime()
    hour = currTime.tm_hour
    minute = currTime.tm_min

    isTimeToWakeUp = (hour>7) or (hour==7 and minute>29)

    if isTimeToWakeUp:
        print("IT IS TIME TO GET UP")

if __name__ == "__main__":
    main()