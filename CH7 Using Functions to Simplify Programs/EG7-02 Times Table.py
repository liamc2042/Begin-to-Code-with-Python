def print_times_tables(multVal):
    count = 1
    while count < 13:
        result = count * multVal
        print(count, 'times', multVal, 'equals', result)
        count += 1

def main():
    print_times_tables(6)

if __name__ == "__main__":
    main()