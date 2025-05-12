import time
import snaps

def main():
    while True:

        currTime = time.localtime()
        hour = str(currTime.tm_hour)
        minute = str(currTime.tm_min)
        second = str(currTime.tm_sec)

        timeStr = hour+':'+minute+':'+second
        snaps.display_message(timeStr)
        time.sleep(1)

if __name__ == "__main__":
    main()