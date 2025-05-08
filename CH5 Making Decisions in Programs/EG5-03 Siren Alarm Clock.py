import time
import snaps

def main():
    currTime = time.localtime()
    hour = currTime.tm_hour
    minute = currTime.tm_min

    if (hour>7) or (hour==7 and minute>29):
        snaps.display_message('TIME TO GET UP')
        snaps.play_sound('siren.wav')
        # Pause to play sound
        time.sleep(10) 

if __name__ == "__main__":
    main()