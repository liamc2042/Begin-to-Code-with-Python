def print_times_tables(multVal, limit):
    count = 1
    while count < limit+1:
        result = count * multVal
        print(count, 'times', multVal, 'equals', result)
        count += 1

def main():
    print_times_tables(6,5)

if __name__ == "__main__":
    main()