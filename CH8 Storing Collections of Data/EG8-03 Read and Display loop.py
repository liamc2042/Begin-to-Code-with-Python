from BTCInput import *

def main():

    sales = []

    for count in range(1, 11):
        prompt = 'Enter the sales for stand ' + str(count) + ': '

        sales.append(read_int(prompt))

    print('Sales figures')

    count = 1

    for sale in sales:
        print('Sales for stand', count, 'are', sale)
        count += 1

if __name__ == '__main__':
    main()