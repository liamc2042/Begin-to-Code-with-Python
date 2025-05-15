def print_times_tables(multVal):
    if isinstance(multVal, int) == False:
        raise Exception('print_times_tables only works with integers')
    count = 1
    while count < 13:
        result = count * multVal
        print(count, 'times', multVal, 'equals', result)
        count += 1

def main():
    print_times_tables(6)

if __name__ == "__main__":
    main()