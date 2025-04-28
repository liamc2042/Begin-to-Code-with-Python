import snaps
import time

def main():
    snaps.display_image('Housemartins.jpg')
    snaps.display_message('Hull Rocks',color=(255,255,255),vert='top')
    time.sleep(5)

if __name__ == "__main__":
    main()