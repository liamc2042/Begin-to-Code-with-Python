import snaps

def main():
    temp = snaps.get_weather_temp(latitude=47.61, longitude=-122.33)

    print('The temperature is:', temp)

    if temp < 40:
        print('Wear a coat - t is cold out there')
    elif temp > 70:
        print('Remember to wear sunscreen')

if __name__ == "__main__":
    main()