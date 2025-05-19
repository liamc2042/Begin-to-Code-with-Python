from BTCInput import *

def main():
    sales = []

    for count in range(1,11):
        prompt = 'Enter the sales for stand ' + str(count) + ':'
        sales.append(read_int(prompt))

    print(sales)

if __name__ == '__main__':
    main()