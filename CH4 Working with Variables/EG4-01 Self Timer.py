import time
import random

def main():
    print("Welcome to Self Timer")
    print()
    print('Everybody Stand Up')
    print('Stay standing until you think the time has ended')
    print('Then sit down.')
    print('Anyone still standing when the time ends loses.')
    print('The last person to sit down before the time ended will win.')
    
    standTime = random.randint(5,20) # Between 5 and 20 seconds

    print('Stay standing for' , standTime, 'seconds.')

    time.sleep(standTime)

    print('****TIME UP****')

if __name__ == "__main__":
    main()