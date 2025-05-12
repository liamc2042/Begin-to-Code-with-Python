def main():
    count = 0
    while count < 5:
        print('Inside loop')
        count += 1
        if count == 3:
            break

    print('Outside loop')
    
if __name__ == "__main__":
    main()