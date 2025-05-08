import snaps

def main():
    desc = snaps.get_weather_desciption(latitude=47.61, longitude=-122.33)
    print("The conditions in Seattle are: ", desc)

if __name__ == "__main__":
    main()