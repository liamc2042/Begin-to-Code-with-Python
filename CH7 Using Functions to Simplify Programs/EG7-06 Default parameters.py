def print_times_tables(multVal, limit=12):
    count = 1
    while count < limit+1:
        result = count * multVal
        print(count, 'times', multVal, 'equals', result)
        count += 1

def main():
    print_times_tables(multVal=7)

if __name__ == "__main__":
    main()