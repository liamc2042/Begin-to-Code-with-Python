import snaps

def main():
    temp = snaps.get_weather_temp(latitude=47.61, longitude=-122.33)
    print("The Temperature in Seattle is: ", temp)

if __name__ == "__main__":
    main()